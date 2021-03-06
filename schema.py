# generated by datamodel-codegen:
#   filename:  schema.json
#   timestamp: 2021-07-19T14:40:21+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class StructuredTextItem(BaseModel):
    rawText: str
    textType: str


class BrandPublication(BaseModel):
    name: str
    firstPublicationDate: str


class BrandSafety(BaseModel):
    is_brandsafe: bool
    confidence: float


class Mention(BaseModel):
    source: str
    index: Optional[int] = None


class Location(BaseModel):
    count: int
    score: float
    country_code: str
    osm_id: int
    place_rank: int
    importance: float
    mentions: List[Mention]
    wikidata: str
    lonlat: List[float]
    name: str


class CustomerIntelligence(BaseModel):
    mensen: float
    binnenland: float
    binnenlandse_politiek: float
    bouwen_en_wonen: float
    bv_nederland: float
    culinair: float
    defensie: float
    digitaal_en_technologie: float
    film_en_podiumkunst: float
    geloof_en_samenleving: float
    gezondheid: float
    herdenken: float
    hoger_onderwijs_en_emancipatie: float
    drama_en_emotie: float
    internationaal: float
    kunst: float
    consumeren_en_besteden: float
    literatuur: float
    muziek: float
    natuur_en_milieu: float
    onderwijs_en_opvoeding: float
    rampen_en_rechtshandhaving: float
    regionieuws: float
    restbak: float
    royalty: float
    sport_overig: float
    televisie: float
    transport: float
    voeding: float
    voetbal: float
    weer: float


class CustomerIntelligenceV2(BaseModel):
    eten_en_drinken: float
    gezondheid_en_zorg: float
    bouwen_en_wonen: float
    religie: float
    technologie_en_handel: float
    consumeren_en_vrije_tijd: float
    het_weer: float
    voetbal: float
    gemeentepolitiek: float
    overheidsbeleid: float
    brand: float
    natuur: float
    maatschappelijke_instellingen: float
    sport: float
    veiligheid: float
    recht_en_justitie: float
    lokale_evenementen: float
    onderwijs: float
    optredens_en_voorstellingen: float
    kunst_en_cultuur: float
    samenleving: float
    verkeersongevallen: float
    bestuur_en_organisatie: float
    verkeer: float
    afval_en_milieuproblematiek: float
    politiek: float
    wielrennen: float
    misdaad: float
    vakbond_club_en_vereniging: float
    relatie_en_opvoeden: float
    economie: float
    zingeving_en_verhalen: float
    nominatie_en_prijzen: float
    duurzaamheid: float
    woon_en_leefomgeving: float
    human_interest: float


class CustomTopics(BaseModel):
    customer_intelligence: CustomerIntelligence
    customer_intelligence_v2: CustomerIntelligenceV2
    lifestyle_topics: List[str]


class MediaTopic(BaseModel):
    id: str
    name: str


class MediaTopicInquiryResult(BaseModel):
    enabled: bool
    mediaTopic: MediaTopic
    score: float


class Mention1(BaseModel):
    end: int
    begin: int


class WikiLink(BaseModel):
    title: str
    id: str
    url: str


class WikiLinkInquiryResult(BaseModel):
    mentions: List[Mention1]
    wikiLink: WikiLink


class WikiLink1(BaseModel):
    title: str
    id: str
    url: str


class NamedEntity(BaseModel):
    type: str
    wikiLink: Optional[WikiLink1] = None
    name: str


class WikiData(BaseModel):
    id: str
    score: str


class Mention2(BaseModel):
    end: int
    begin: int


class NamedEntityInquiryResult(BaseModel):
    namedEntity: NamedEntity
    score: float
    saliency: float
    keyword: bool
    confidence: str
    altNames: List
    wikiData: Optional[WikiData] = None
    mentions: List[Mention2]


class Semantics(BaseModel):
    mediaTopicInquiryResults: List[MediaTopicInquiryResult]
    wikiLinkInquiryResults: List[WikiLinkInquiryResult]
    namedEntityInquiryResults: List[NamedEntityInquiryResult]


class ItemUrl(BaseModel):
    brand: str
    url: str


class Enrichments(BaseModel):
    brand_safety: BrandSafety
    locations: List[Location]
    NSentences: int
    GensimDocumentEmbedding: List[float]
    CustomTopics: CustomTopics
    raw_character_count: int
    NWords: int
    Sentiment: List[float]
    MinHash: List[int]
    Complexity: float
    semantics: Semantics
    Language: str
    item_urls: List[ItemUrl]
    urgency: float
    CleanText: str
    creator_brand: str
    subdesk: Optional[str] = None
    desk: Optional[str] = None


class Caption(BaseModel):
    html_text: str
    raw_text: str
    html_annotations: List
    raw_annotations: List


class PhotoLink(BaseModel):
    provider: str
    id: int


class FocusPoint(BaseModel):
    x: float
    y: float


class Asset1(BaseModel):
    media_pools: Optional[List] = None
    asset_entity_id: str
    crops: Optional[List] = None
    caption: Optional[Caption] = None
    photo_link: Optional[PhotoLink] = None
    asset_type: str
    xxl_crop: Optional[bool] = None
    credit: Optional[str] = None
    author: Optional[str] = None
    focus_point: Optional[FocusPoint] = None


class Asset(BaseModel):
    assetId: str
    asset: Asset1


class Item(BaseModel):
    publicationDate: str
    structuredText: List[StructuredTextItem]
    firstPublicationDate: str
    contentType: str
    mainSection: str
    publicationTimeStamp: int
    brand: str
    label: Optional[str] = None
    url: str
    brandPublications: List[BrandPublication]
    title: str
    articleType: str
    schemaVersion: str
    published: bool
    majorVersion: str
    enrichments: Enrichments
    payWall: bool
    articleId: int
    author: str
    assets: List[Asset]
    sectionPath: str
    imageUrlLarge: str
    category: str
    imageUrl: str
    shortId: str
    authorNames: List[str]
    minorVersion: str
    brands: List[str]
    subLabel: Optional[str] = None


class ItemEnrichments(BaseModel):
    timestamp: str
    component: str
    version: str


class Metadata(BaseModel):
    item_enrichments: ItemEnrichments = Field(..., alias='item.enrichments')


class Model(BaseModel):
    item: Item
    metadata: Metadata
