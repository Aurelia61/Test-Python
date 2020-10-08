
    @staticmethod
    def import_image(image_link):
        """
            imports an image
        """
    
        imported_image = pygame.image.load(image_link)
        return imported_image


    @staticmethod
    def show_image(screen: pygame.Surface, image, image_place_width = 0, image_place_height = 0 ):
        """
            shows an image on a specific place on window
        """
        screen.blit(image, (image_place_width, image_place_height))

    @staticmethod
    def update_window():
        """
            updates the window
        """
        pygame.display.flip()