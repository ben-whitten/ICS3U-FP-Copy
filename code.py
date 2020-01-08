# Created by: Ben Whitten
# Created by: Joey Marcotte & Ben Whitten
# Created on: December 2019
# This file is the "Jungle Joe and Snakob" game
# for CircuitPython
@@ -197,68 +197,91 @@ def game_splash_scene():
        # update game logic
        time.sleep(1.0)
        main_menu_scene()
        # redraw sprite list
        pass # just a placeholder until you write the code


def main_menu_scene():
    # this function is the main menu scene
    text = []
    sprites = []
    sun = []

    image_bank_5 = stage.Bank.from_bmp16("Backgrounds.bmp")
    image_bank_5 = stage.Bank.from_bmp16("backgrounds.bmp")
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_5, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    background.tile(2, 8, 1)
    background.tile(2, 8, 2)
    background.tile(2, 8, 3)
    background.tile(2, 8, 4)
    background.tile(2, 8, 5)
    background.tile(2, 8, 6)
    background.tile(2, 8, 7)
    background.tile(2, 8, 8)
    background.tile(2, 8, 9)
    background.tile(2, 8, 10)

    text_1 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_1.move(40, 35)
    text_1.move(40, 48)
    text_1.text("JUNGLE JOE")
    text.append(text_1)

    text_2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_2.move(40, 45)
    text_2.move(40, 58)
    text_2.text("& SNAKOB'S")
    text.append(text_2)

    text_3 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_3.move(25, 55)
    text_3.move(25, 68)
    text_3.text("BONGO BANANZA!")
    text.append(text_3)
    

    text_4 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_4.move(35, 118)
    text_4.text("PRESS START!")
    text.append(text_4)

    # Displays the tree tops
    tree_top_1 = stage.Sprite(image_bank_5, 1, 0, 112)
    sprites.append(tree_top_1)
    tree_top_2 = stage.Sprite(image_bank_5, 1, 16, 112)
    sprites.append(tree_top_2)
    tree_top_3 = stage.Sprite(image_bank_5, 1, 32, 112)
    sprites.append(tree_top_3)
    tree_top_4 = stage.Sprite(image_bank_5, 1, 48, 112)
    sprites.append(tree_top_4)
    tree_top_5 = stage.Sprite(image_bank_5, 1, 64, 112)
    sprites.append(tree_top_5)
    tree_top_6 = stage.Sprite(image_bank_5, 1, 80, 112)
    sprites.append(tree_top_6)
    tree_top_7 = stage.Sprite(image_bank_5, 1, 96, 112)
    sprites.append(tree_top_7)
    tree_top_8 = stage.Sprite(image_bank_5, 1, 112, 112)
    sprites.append(tree_top_8)
    tree_top_9 = stage.Sprite(image_bank_5, 1, 128, 112)
    sprites.append(tree_top_9)
    tree_top_10 = stage.Sprite(image_bank_5, 1, 144, 112)
    sprites.append(tree_top_10)
    # Displays the sun
    sun_top_left = stage.Sprite(image_bank_5, 11, 128, 0)
    sun.append(sun_top_left)
    sun_top_right = stage.Sprite(image_bank_5, 10, 144, 0)
    sun.append(sun_top_right)
    sun_bottom_left = stage.Sprite(image_bank_5, 8, 128, 16)
    sun.append(sun_bottom_left)
    sun_bottom_right = stage.Sprite(image_bank_5, 9, 144, 16)
    sun.append(sun_bottom_right)
    # Displays Jungle Joe
    jungle_joe = stage.Sprite(image_bank_3, 15, 71, 98)
    sprites.append(jungle_joe)

    clouds = []
    for cloud_number in range(constants.TOTAL_CLOUDS):
        a_single_cloud = stage.Sprite(image_bank_5, 5, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        a_single_cloud = stage.Sprite(image_bank_5, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        clouds.append(a_single_cloud)

    def Show_clouds():
        for cloud_number in range(len(clouds)):
            if clouds[cloud_number].x < 20:
                clouds[cloud_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_Y - constants.SPRITE_SIZE), constants.OFF_LEFT_SCREEN)
            if clouds[cloud_number].x > constants.SCREEN_X + constants.SPRITE_SIZE or clouds[cloud_number].x < constants.OFF_LEFT_SCREEN:
                clouds[cloud_number].move(constants.OFF_LEFT_SCREEN, random.randint(0, constants.SCREEN_Y - constants.SPRITE_SIZE))
                break

    cloud_count = 6
    Show_clouds()
    Show_clouds()

    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + clouds + [background]
    game.layers = text + sprites + clouds + sun + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    # wait until refresh rate finishes
@@ -267,25 +290,86 @@ def Show_clouds():
    # repeat forever, game loop
    while True:
        # get user input

        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_START != 0:  # Start button
            game_scene()

        # update game logic
        for cloud_number in range (len(clouds)):
            if clouds[cloud_number].y > 0:
                clouds[cloud_number].move(clouds[cloud_number].x,
                clouds[cloud_number].move(clouds[cloud_number].x
                                          + constants.CLOUD_SPEED,
                                          clouds[cloud_number].y)
                if clouds[cloud_number].x > constants.SCREEN_X:
                if clouds[cloud_number].x > constants.SCREEN_X + constants.SPRITE_SIZE:
                    clouds[cloud_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    Show_clouds()
                if clouds[cloud_number].x > constants.SCREEN_X/2:
                if clouds[cloud_number].x > constants.SCREEN_X / 2:
                    Show_clouds()
        # redraw sprite list
        pass # just a placeholder until you write the code

        game.render_sprites(clouds)
        game.tick()

def game_scene():
    # this function is the game scene
    border = []
    sprites = []
    image_bank_5 = stage.Bank.from_bmp16("backgrounds.bmp")
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")

    background = stage.Grid(image_bank_5, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_2_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(2,3)
            background.tile(x_location, y_location, tile_picked)
    for x_location in range(constants.SCREEN_GRID_2_X, constants.SCREEN_GRID_3_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 5)

    # Displays the border.
    border_1 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 0)
    border.append(border_1)
    border_2 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 16)
    border.append(border_2)
    border_3 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 32)
    border.append(border_3)
    border_4 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 48)
    border.append(border_4)
    border_5 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 64)
    border.append(border_5)
    border_6 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 80)
    border.append(border_6)
    border_7 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 96)
    border.append(border_7)
    border_8 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 112)
    border.append(border_8)

    # Displays key sprites.
    a_button = stage.Sprite(image_bank_3, 12, constants.A_BUTTON_LOCATION, constants.BUTTON_HEIGHT)
    sprites.append(a_button)
    b_button = stage.Sprite(image_bank_3, 11, constants.B_BUTTON_LOCATION, constants.BUTTON_HEIGHT)
    sprites.append(b_button)
    left_arrow = stage.Sprite(image_bank_3, 8, constants.LEFT_ARROW_LOCATION, constants.BUTTON_HEIGHT)
    sprites.append(left_arrow)
    right_arrow = stage.Sprite(image_bank_3, 7, constants.RIGHT_ARROW_LOCATION, constants.BUTTON_HEIGHT)
    sprites.append(right_arrow)
    up_arrow = stage.Sprite(image_bank_3, 10, constants.UP_ARROW_LOCATION, constants.BUTTON_HEIGHT)
    sprites.append(up_arrow)
    down_arrow = stage.Sprite(image_bank_3, 9, constants.DOWN_ARROW_LOCATION, constants.BUTTON_HEIGHT)
    sprites.append(down_arrow)


    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + border + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

# repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # redraw sprite list
        pass # just a placeholder until you write the code

def game_over_scene(final_score):
    # this function is the game over scene
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # redraw sprite list
        pass # just a placeholder until you write the code

if __name__ == "__main__":
    blank_white_reset_scene()
    # blank_white_reset_scene()
