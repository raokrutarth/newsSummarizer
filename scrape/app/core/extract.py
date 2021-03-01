import logging
from datetime import datetime
from enum import Enum
from typing import List, Union

import newspaper
from cleantext import clean as text_clean
from data_models.extract import ExtractResult
from goose3 import Goose
from htmldate import find_date

log = logging.getLogger(__name__)


class Strategy(Enum):
    auto_scraper = "auto_scraper"
    goose = "goose"
    news_paper = "news_paper"


class Scraper(object):
    @staticmethod
    def scrape(
        strategy: Strategy, url: str, tags: List[str]
    ) -> Union[ExtractResult, None]:

        try:
            if strategy is Strategy.news_paper:
                return Scraper._scrape_newspaper(url, tags)
            else:
                log.error(f"Scraper for strategy {strategy} not implemented.")
        except Exception:
            log.exception(
                f"Failed to scrape article in URL {url} and tags {tags} with exception."
            )

        return None

    def scrape_v0(self, url: str) -> str:
        # TODO train scraper properly
        # url = "https://medium.com/@Medium/statistics-2971adaa615"
        # wanted_list = [
        #     "What I failed to notice is if someone scraped a different IMDb page than I did, they’d possibly have missing metascore ",
        #     "data there, and once we scraped multiple pages in this guide, we’ll have missing metascore data as well."
        #     "There you have it! We’ve successfully extracted data of the top",
        #     "https://miro.medium.com/max/627/1*PJ6-gXGMdHJmbi9jUChn3g.png",
        #     "https://miro.medium.com/max/2528/0*1RlS1lN-dt4Igp1J.png",
        # ]

        # scraper = AutoScraper()
        # scraper.build(url, wanted_list)

        # content = scraper.get_result_similar(
        #     url, contain_sibling_leaves=True, keep_order=True
        # )
        # return ExtractResult(
        #     title="",
        #     raw_text=content,
        #     images=[],
        #     date_fetched=datetime.now(),
        #     date_published=find_date(url),
        #     url=url,
        # )
        return ""

    @staticmethod
    def scrape_vx(url: str) -> ExtractResult:
        config = {}
        config["strict"] = False  # turn of strict exception handling
        config["browser_user_agent"] = "Mozilla 5.0"  # set the browser agent string
        config["http_timeout"] = 5.05  # set http timeout in seconds

        with Goose(config) as g:
            article = g.extract(url=url)
            return ExtractResult(
                title=article.title,
                raw_text=article.cleaned_text,
                images=[],
                date_fetched=datetime.now(),
                date_published=find_date(url),
                url=url,
            )

    @staticmethod
    def _scrape_newspaper(url: str, tags: List[str] = []) -> ExtractResult:
        """
        TODO thid does a file lock on tldextract.json.lock. Fix for performance.
        """
        article = newspaper.Article(url)
        article.download()
        article.parse()
        # article.nlp()  # do basic keyword extraction
        page = newspaper.build(url)

        cleaned_content = text_clean(
            article.text,
            lang="en",  # set to 'de' for German special handling
            fix_unicode=True,  # fix various unicode errors
            to_ascii=True,  # transliterate to closest ASCII representation
            no_line_breaks=False,  # fully strip line breaks as opposed to only normalizing them
            no_urls=False,  # replace all URLs with a special token
            no_emails=False,  # replace all email addresses with a special token
            no_phone_numbers=False,  # replace all phone numbers with a special token
            no_numbers=False,  # replace all numbers with a special token
            no_digits=False,  # replace all digits with a special token
            no_currency_symbols=False,  # replace all currency symbols with a special token
            no_punct=False,  # remove punctuations
            replace_with_url="<URL>",
            # replace_with_punct="",          # instead of removing punctuations you may replace them
            lower=False,  # lowercase text
            # replace_with_email="<EMAIL>",
            # replace_with_phone_number="<PHONE>",
            # replace_with_number="<NUMBER>",
            # replace_with_digit="0",
            # replace_with_currency_symbol="<CUR>",
        )

        return ExtractResult(
            title=article.title,
            raw_text=cleaned_content,
            images=article.images,
            date_fetched=datetime.now(),
            date_published=article.publish_date,
            url=url,
            nested_urls=page.category_urls(),
            tags=tags,
            is_cleaned=True,
        )

    def scrape_v3(self, url: str) -> str:
        # response = requests.get(url)
        # paragraphs = justext.justext(response.content, justext.get_stoplist("English"))

        # content = ""
        # for paragraph in paragraphs:
        #     if not paragraph.is_boilerplate:
        #         content += paragraph.text + "\n"

        # return ExtractResult(
        #     title="",
        #     raw_text=content,
        #     images=[],
        #     date_fetched=datetime.now(),
        #     date_published=find_date(url),
        #     url=url,
        # )
        return ""

    def scrape_pdf(self, url: str):
        # TODO use Textract to parse PDFs
        raise NotImplementedError

    def scrape_images(self, url: str):
        # TODO use Lassie to get images
        raise NotImplementedError
