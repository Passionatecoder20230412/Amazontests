from pages.HomeIconsNavigationStatus import HomeIconsNavigationStatus


class TestHomeIcons:

    def test_home_icons(self,init_driver):

        icons=HomeIconsNavigationStatus(init_driver)
        icons.icons_list()