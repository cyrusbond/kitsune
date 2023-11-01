import pytest
import pytest_check as check
import requests

from selenium_tests.core.test_utilities import TestUtilities
from selenium_tests.messages.contribute_pages_messages.con_forum_page_messages import (
    ContributeForumMessages,
)
from selenium_tests.messages.contribute_pages_messages.con_help_articles_page_messages import (
    ContributeHelpArticlesMessages,
)
from selenium_tests.messages.contribute_pages_messages.con_localization_page_messages import (
    ContributeLocalizationMessages,
)
from selenium_tests.messages.contribute_pages_messages.con_mobile_support_page_messages import (
    ContributeMobileSupportMessages,
)
from selenium_tests.messages.contribute_pages_messages.con_page_messages import (
    ContributePageMessages,
)
from selenium_tests.messages.contribute_pages_messages.con_social_support_messages import (
    ContributeSocialSupportMessages,
)
from selenium_tests.messages.homepage_messages import HomepageMessages


class TestContributeMobilePage(TestUtilities):
    #  C2176366
    @pytest.mark.contributePagesTests
    def test_contribute_mobile_page_text(self):
        self.logger.info("Accessing the Contribute Mobile Store page")
        self.pages.ways_to_contribute_pages.navigate_to(
            ContributeMobileSupportMessages.STAGE_CONTRIBUTE_MOBILE_SUPPORT_PAGE_URL
        )

        self.logger.info(
            "Verifying that the Contribute Mobile Store page contains the correct strings"
        )

        check.equal(
            self.pages.ways_to_contribute_pages.get_hero_main_header_text(),
            ContributeMobileSupportMessages.HERO_PAGE_TITLE,
            f"Text is: {self.pages.ways_to_contribute_pages.get_hero_main_header_text()}"
            f"Expected: {ContributeMobileSupportMessages.HERO_PAGE_TITLE}",
        )

        check.equal(
            self.pages.ways_to_contribute_pages.get_hero_second_header_text(),
            ContributeMobileSupportMessages.HERO_SECOND_TITLE,
            f"Text is: {self.pages.ways_to_contribute_pages.get_hero_second_header_text()}"
            f"Expected: {ContributeMobileSupportMessages.HERO_SECOND_TITLE}",
        )

        check.equal(
            self.pages.ways_to_contribute_pages.get_hero_text(),
            ContributeMobileSupportMessages.HERO_TEXT,
            f"Text is: {self.pages.ways_to_contribute_pages.get_hero_text()}"
            f"Expected: {ContributeMobileSupportMessages.HERO_TEXT}",
        )

        check.equal(
            self.pages.ways_to_contribute_pages.get_how_to_contribute_header_text(),
            ContributeMobileSupportMessages.HOW_TO_CONTRIBUTE_HEADER,
            f"Text is: {self.pages.ways_to_contribute_pages.get_how_to_contribute_header_text()}"
            f"Expected is: {ContributeMobileSupportMessages.HOW_TO_CONTRIBUTE_HEADER}",
        )

        # Need to add a check for the logged in state as well.
        # Excluding option four from the list since we are using a different locator

        card_titles = [
            ContributeMobileSupportMessages.HOW_TO_CONTRIBUTE_OPTION_ONE_SIGNED_OUT,
            ContributeMobileSupportMessages.HOW_TO_CONTRIBUTE_OPTION_TWO,
            ContributeMobileSupportMessages.HOW_TO_CONTRIBUTE_OPTION_THREE,
            ContributeMobileSupportMessages.HOW_TO_CONTRIBUTE_OPTION_FIVE,
        ]

        check.equal(
            self.pages.ways_to_contribute_pages.get_how_to_contribute_link_options_text(),
            card_titles,
            "How you can contribute steps are incorrect!",
        )

        check.equal(
            self.pages.ways_to_contribute_pages.get_how_to_contribute_option_four_text(),
            ContributeMobileSupportMessages.HOW_TO_CONTRIBUTE_OPTION_FOUR,
            f"Text is: "
            f"{self.pages.ways_to_contribute_pages.get_how_to_contribute_option_four_text()}"
            f"Expected is: "
            f"{ContributeMobileSupportMessages.HOW_TO_CONTRIBUTE_OPTION_FOUR}",
        )

        check.equal(
            self.pages.ways_to_contribute_pages.get_first_fact_text(),
            ContributeMobileSupportMessages.FACT_FIRST_LINE,
            f"Text is: {self.pages.ways_to_contribute_pages.get_first_fact_text()}"
            f"Expected is: {ContributeMobileSupportMessages.FACT_FIRST_LINE}",
        )

        check.equal(
            self.pages.ways_to_contribute_pages.get_second_fact_text(),
            ContributeMobileSupportMessages.FACT_SECOND_LINE,
            f"Text is: {self.pages.ways_to_contribute_pages.get_second_fact_text()}"
            f"Expected is: {ContributeMobileSupportMessages.FACT_SECOND_LINE}",
        )

        check.equal(
            self.pages.ways_to_contribute_pages.get_other_ways_to_contribute_header_text(),
            ContributeMobileSupportMessages.OTHER_WAYS_TO_CONTRIBUTE_HEADER,
            f"Text is: "
            f"{self.pages.ways_to_contribute_pages.get_other_ways_to_contribute_header_text()}"
            f"Expected is: "
            f"{ContributeMobileSupportMessages.OTHER_WAYS_TO_CONTRIBUTE_HEADER}",
        )

        other_ways_to_contribute_card_titles = [
            ContributeMobileSupportMessages.ANSWER_QUESTIONS_IN_SUPPORT_FORUM_TITLE_CARD_TITLE,
            ContributeMobileSupportMessages.WRITE_HELP_ARTICLES_CARD_TITLE,
            ContributeMobileSupportMessages.LOCALIZE_CONTENT_CARD_TITLE,
            ContributeMobileSupportMessages.PROVIDE_SUPPORT_ON_SOCIAL_CHANNELS_CARD_TITLE,
        ]

        check.equal(
            self.pages.ways_to_contribute_pages.get_other_ways_to_contribute_card_titles_text(),
            other_ways_to_contribute_card_titles,
            "Other ways to contribute card titles are not the correct ones!",
        )

    # C2176366
    @pytest.mark.contributePagesTests
    def test_contribute_mobile_page_images_are_not_broken(self):
        self.logger.info("Accessing the Contribute Mobile store page")
        self.pages.ways_to_contribute_pages.navigate_to(
            ContributeMobileSupportMessages.STAGE_CONTRIBUTE_MOBILE_SUPPORT_PAGE_URL
        )

        self.logger.info("Verifying that the Contribute Mobile store page images are not broken")

        for link in self.pages.ways_to_contribute_pages.get_all_page_image_links():
            image_link = link.get_attribute("src")
            response = requests.get(image_link, stream=True)
            check.is_true(response.status_code < 400, f"The {image_link} image is broken")

    # C2176367
    @pytest.mark.contributePagesTests
    def test_contribute_mobile_page_breadcrumbs(self):
        self.logger.info("Accessing the Contribute Mobile Store page")
        self.pages.ways_to_contribute_pages.navigate_to(
            ContributeMobileSupportMessages.STAGE_CONTRIBUTE_MOBILE_SUPPORT_PAGE_URL
        )

        self.logger.info("Verifying that the correct breadcrumbs are displayed")
        breadcrumbs = [
            ContributeMobileSupportMessages.FIRST_BREADCRUMB,
            ContributeMobileSupportMessages.SECOND_BREADCRUMB,
            ContributeMobileSupportMessages.THIRD_BREADCRUMB,
        ]

        check.equal(
            self.pages.ways_to_contribute_pages.get_text_of_all_breadcrumbs(),
            breadcrumbs,
            f"Breadcrumbs are: {self.pages.ways_to_contribute_pages.get_text_of_all_breadcrumbs()}"
            f"Expected: {breadcrumbs}",
        )

        counter = 1
        for breadcrumb in self.pages.ways_to_contribute_pages.get_all_interactable_breadcrumbs():
            breadcrumb_to_click = (
                self.pages.ways_to_contribute_pages.get_all_interactable_breadcrumbs()[counter]
            )
            self.pages.ways_to_contribute_pages.click_on_breadcrumb(breadcrumb_to_click)

            if counter == 1:
                self.logger.info(
                    "Verifying that the Contribute breadcrumb redirects to the Contribute page"
                )
                check.equal(
                    self.pages.contribute_page.current_url(),
                    ContributePageMessages.STAGE_CONTRIBUTE_PAGE_URL,
                    f"Expected to be on {ContributePageMessages.STAGE_CONTRIBUTE_PAGE_URL}"
                    f"We are actual on {self.pages.contribute_page.current_url()}",
                )
                self.pages.contribute_page.navigate_forward()
                counter -= 1
            elif counter == 0:
                self.logger.info("Verifying that the Home breadcrumb redirects to the Homepage")
                check.equal(
                    self.pages.homepage.current_url(),
                    HomepageMessages.STAGE_HOMEPAGE_URL,
                    f"Expected to be on {HomepageMessages.STAGE_HOMEPAGE_URL}"
                    f"We are actual on {self.pages.homepage.current_url()}",
                )

    # Need to add tests for "How you can contribute" section

    # C2176370
    @pytest.mark.contributePagesTests
    def test_contribute_mobile_other_ways_to_contribute_redirect_to_the_correct_page(self):
        self.logger.info("Accessing the Contribute Mobile Store page")
        self.pages.ways_to_contribute_pages.navigate_to(
            ContributeMobileSupportMessages.STAGE_CONTRIBUTE_MOBILE_SUPPORT_PAGE_URL
        )

        self.logger.info(
            "Verifying that the 'other ways to contribute' "
            "cards are redirecting to the correct SUMO page"
        )

        ways_to_contribute_links = [
            ContributeForumMessages.STAGE_CONTRIBUTE_FORUM_PAGE_URL,
            ContributeHelpArticlesMessages.STAGE_CONTRIBUTE_HELP_ARTICLES_PAGE_URL,
            ContributeLocalizationMessages.STAGE_CONTRIBUTE_LOCALIZATION_PAGE_URL,
            ContributeSocialSupportMessages.STAGE_CONTRIBUTE_SOCIAL_SUPPORT_PAGE_URL,
        ]

        counter = 0
        for (
            element
        ) in self.pages.ways_to_contribute_pages.get_all_other_ways_to_contribute_card_list():
            card = (
                self.pages.ways_to_contribute_pages.get_all_other_ways_to_contribute_card_list()[
                    counter
                ]
            )
            self.pages.ways_to_contribute_pages.click_on_other_way_to_contribute_card(card)
            check.equal(
                ways_to_contribute_links[counter],
                self.pages.ways_to_contribute_pages.current_url(),
                f"Expected the following URL: {ways_to_contribute_links[counter]}"
                f"Received: {self.pages.ways_to_contribute_pages.current_url()}",
            )
            self.pages.contribute_page.navigate_back()
            counter += 1