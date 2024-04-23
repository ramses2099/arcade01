import arcade

def main():
    arcade.open_window(600, 600, "test")
    
    arcade.set_background_color(arcade.color.WHITE)
    
    arcade.start_render()
    
    arcade.finish_render()
    
    arcade.run()

if __name__ == "__main__":
    main()