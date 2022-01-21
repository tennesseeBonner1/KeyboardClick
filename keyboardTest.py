from pynput.keyboard import Key, Listener
import pygame

def ps(key):
	sfx.play()

	if key == Key.esc:
		return False

if __name__ == '__main__':
	pygame.mixer.init()
	sfx = pygame.mixer.Sound('Keyboard.wav')
	with Listener(on_press = ps) as listener:
		listener.join()


	
