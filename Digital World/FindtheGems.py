from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.core.window import Window 
from kivy.graphics import Rectangle
import random

class StartScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.state = 0
        self.layout = FloatLayout()
        
        # Title
        title = Label(text = "Welcome to the Game! Press start to play!",
                           font_size = 30,
                           pos_hint={'x': 0.005, 'top': 1.3})
        self.layout.add_widget(title)
        
        #  Start Button
        b_start = Button(text = "Start Game", 
                      background_color=(50, 50, 0, 0.9),
                      font_size = 20,
                      pos_hint={'x': 0.4, 'top': 0.5}, 
                      size_hint = (0.2, 0.1),
                      on_press = self.jump)
        self.layout.add_widget(b_start)
        
        # Quit Button
        b_quit = Button(text = "Quit", 
                       font_size = 20,
                       pos_hint={'x': 0.8, 'top': 0.1},
                       size_hint = (0.2, 0.1),
                       on_press = self.quit_game)
        self.layout.add_widget(b_quit)
        
        self.add_widget(self.layout)        
        
    # Jumping start button that changes colour randomly
    def jump(self, instance): 
        if self.state == 0:
            instance.text = "Starting"
            instance.pos_hint = {'x': random.uniform(0,0.8), 'top': random.uniform(0.2,0.8)}
            instance.background_color=(random.choice([(50,0,0,0.9),(0,50,0,0.9),(0,0,50,0.9),
                                                      (50,50,0,0.9),(50,0,50,0.9),(0,50,50,0.9)]))
            self.state = 1
            self.counter = 1
        elif self.state == 1:
            instance.pos_hint = {'x': random.uniform(0,0.8), 'top': random.uniform(0.2,0.8)}
            instance.background_color=(random.choice([(50,0,0,0.9),(0,50,0,0.9),(0,0,50,0.9),
                                                      (50,50,0,0.9),(50,0,50,0.9),(0,50,50,0.9)]))
            self.counter += 1
            if self.counter == 4:
                instance.text = "Finally start!"
                instance.pos_hint = {'x': random.uniform(0,0.8), 'top': random.uniform(0.2,0.8)}
                instance.background_color=(random.choice([(50,0,0,0.9),(0,50,0,0.9),(0,0,50,0.9),
                                                      (50,50,0,0.9),(50,0,50,0.9),(0,50,50,0.9)]))
                instance.bind(on_press=self.change_to_game)
                self.state == 2

    def change_to_game(self, value):
        self.manager.transition.direction = 'left'
        self.manager.current = "game"

    def quit_game(self, value):
        App.get_running_app().stop()
        Window.close()
        
class GameScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.state = 0
        
        # Player
        with self.canvas:
            self.player = Player(pos = (0,50),
                                 size = (50,50))
            
        # Input parameters
        self.player.name = input('What is your name')
        lives = input('How many lives do you want to start with?')
        try:
            self.player.health = int(lives)
        except ValueError:
            lives = input('Sorry, please input an integer in numerical form')
        goal = input('How many gems do you want to find?')
        try:
            self.player.goal = int(goal)
        except ValueError:
            lives = input('Sorry, please input an integer in numerical form')
        
            
        # Maze
        self.maze = ['***************',
                     '********    @ *',
                     '*      @ ******',
                     '* *************',
                     '* ******    ***',
                     '*   @    ******',
                     '* ** *** ******',
                     '**   ***    ***',
                     '*  ********@ **',
                     '***************']
        l_maze = BoxLayout(orientation = 'vertical')
        for bgd_row in self.maze:
            row = BoxLayout(orientation = 'horizontal')
            l_maze.add_widget(row)
            for col in bgd_row:
                if col == '*':
                    row.add_widget(Button(background_color = (0,1,0,1)))
                elif col == '@':
                    row.add_widget(Button(text = 'life',
                                          font_size = 15,
                                          background_color = (0,0,1,1)))
                else:
                    row.add_widget(Button(background_color = (1,1,0,1)))
        self.layout.add_widget(l_maze)
        
        # Text
        self.l_inventory = Label(text = "Player:" + str(self.player.name) + "Health:" + str(self.player.health) + "Gem:" + str(self.player.inventory['gem']), 
                         font_size = 20,
                         pos_hint={'x': 0, 'top': 0.1},
                         size_hint = (1, 0.05))  
        self.layout.add_widget(self.l_inventory)

        # Back Button
        bback = Button(text = "Quit", 
                       font_size = 20,
                       pos_hint={'x': 0, 'top': 0.1},
                       size_hint = (1, 0.05),
                       on_press = self.quit_game)
        self.layout.add_widget(bback)
        self.add_widget(self.layout)
        
        # Keyboard WASD
        self._keyboard = Window.request_keyboard(None,self)
        self._keyboard.bind(on_key_down = self._on_key_down)
        self._keyboard.bind(on_key_up = self._on_key_up)
        self.keysPressed = set() 
    
        
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(text)
        newx = self.player.pos[0]
        newy = self.player.pos[1]
        if 'w' in self.keysPressed and newy < 500:
            newy += 50
        elif newy >= 500:
            newy = 500
        if 's' in self.keysPressed and newy > 50:
            newy -= 50
        elif newy <= 50:
            newy = 50
        if 'a' in self.keysPressed and newx > 0:
            newx -= 50
        elif newx <= 0:
            newx = 0
        if 'd' in self.keysPressed and newx < 700:
            newx += 50
        elif newx >= 700:
            newx = 700
        self.player.pos = (newx, newy)
                        
        # Check for collision
        col = int(self.player.pos[0] // 50)
        row = 9 - int((self.player.pos[1]-50) // 50)
        print(self.player.pos, 'and', (row,col))
        if self.maze[row][col] == '*':
            print('colliding')
            # Drop Rate (Gem, potion, poison)
            if random.random() < 0.3:
                self.player.inventory['gem'] += 1           
            elif random.random() < 0.4:
                self.player.health -= 1
            if self.player.health <= 0:
                self.manager.transition.direction = 'left'
                self.manager.current = "lose"
            if self.player.inventory['gem'] >= self.player.goal:
                self.manager.transition.direction = 'left'
                self.manager.current = "win"
        elif self.maze[row][col] == '@':
            print('Life!')
            self.player.health += 1
        else:
            print('not colliding')
        self.l_inventory.text = "Player:" + str(self.player.name) + "Health:" + str(self.player.health) + "Gem:" + str(self.player.inventory['gem'])
    
    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    def quit_game(self, value):
        App.get_running_app().stop()
        Window.close()
        
class WinScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = FloatLayout()
                
        #Title
        title = Label(text = 'Yay you found the gems! Quit and play again!',
                           font_size = 30,
                           pos_hint={'x': 0.005, 'top': 1.3})
        self.layout.add_widget(title)
        
        # Quit Button
        bquit = Button(text = 'Quit',
                        font_size = 18,
                        background_color = (0, 50, 0, 0.9),
                        pos_hint = {'x': 0.4, 'top': 0.5},
                        size_hint = (0.2, 0.1),
                        on_press = self.quit_game)
        self.layout.add_widget(bquit)
        
        self.add_widget(self.layout)

    def quit_game(self, value):
        App.get_running_app().stop()
        Window.close()   

class LoseScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = FloatLayout()
                
        #Title
        title = Label(text = 'Oh no, you have died! Quit and play again!',
                           font_size = 30,
                           pos_hint={'x': 0.005, 'top': 1.3})
        self.layout.add_widget(title)
        
        # Quit Button
        bquit = Button(text = 'Quit',
                        font_size = 18,
                        background_color = (50, 0, 0, 0.9),
                        pos_hint={'x': 0.4, 'top': 0.5},
                        size_hint = (0.2, 0.1),
                        on_press = self.quit_game)
        self.layout.add_widget(bquit)
        
        self.add_widget(self.layout)

    def quit_game(self, value):
        App.get_running_app().stop()
        Window.close()        

class Player(Rectangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inventory = {'potion': 0, 'gem': 0}
        self.name = 'player'
        self.health = 3

player = Player()

class SwitchScreenApp(App):
    def build(self):
            SM = ScreenManager()
            s1 = StartScreen(name = 'menu')
            s2 = GameScreen(name = 'game')
            s3 = WinScreen(name = 'win')
            s4 = LoseScreen(name = 'lose')
            SM.add_widget(s1)
            SM.add_widget(s2)
            SM.add_widget(s3)
            SM.add_widget(s4)
            SM.current = 'menu'
            Window.size = (750, 550)
            return SM


SwitchScreenApp().run()
