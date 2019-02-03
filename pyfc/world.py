'''
world.py

This is the file that will be imported by the client bot

@yashbonde - 15.01.2019
'''

from .inference_handler import InferenceHandler

# utils
from .utils.attr_handler import AttrHandler
from .utils.display_utils import show_status
from .utils.config_utils import read_config_file, write_config_file
from .utils.attr_lists import REQ_GAME_ATTR

class World(object):
	'''
	Python binding for Freeciv 3.1

	Implementation details and specs are given in READMEs
	'''
	def __init__(self):
		'''
		This is where we initialize the main class 
		Args:
		'''
		# Core gameplay attributes - game attributes
		self.plyr_civ = None

		# Core gameplay attributes (ops) - game attributes that are for the game mech
		self.is_running = False
		self.plyr_id = None # player ID given by the server
		self.unit2key = None # dictionary converting int key to string key

		# Core back attributes
		self.GameATTR = AttrHandler
		self.masterHandler = InferenceHandler

	### BASE FUNCTIONS ####
	'''
	These are the functions that run in the standard loop. All the functions
	names should start with underscore
	'''

	def _save_game(self):
		'''
		This is the function that saves the game periodically
		'''
		self.masterHandler.save_game()
		pass

	def _set_attributes_from_ifHandler(self):
		# once the inference handler is done inference-ing (:P)
		pass

	def _show_infr_handler_status(self):
		attr_value_dict = self.masterHandler.ATTR.get_attr_value_dict()
		show_status('InferenceHandler', attr_value_dict)

	def _show_world_status(self):
		attr_value_dict = self.ATTR.get_attr_value_dict()
		show_status('World', attr_value_dict)

	def _show_network_status(self):
		attr_value_dict = self.masterHandler.fcio.ATTR.get_attr_value_dict()
		show_status('Network', attr_value_dict)
		


	## BASE FUNCTION OVERRIDERS ##
	'''
	These are the functions that can be called by the client as his wish, these are same
	as the base functions but override the 
	'''
	
	def save_game(force):
		'''
		This overrides the save loop by calling _save_game() function
		'''
		self._save_game()

	#### MAIN FUNCTIONS (GAMEPLAY) ####
	'''
	These are the functions that are related to gameplay
	'''
	def get_units_list(self):
		'''
		return list of all units
		'''
		return self.masterHandler.get_units_list(key = 'all')

	def get_unit_by_key(self, key):
		return self.masterHandler.get_units_list(key = self.unit2key[key])
		

	def show_unit_status(self, unit):
		'''
		Show the status and details of unit (int)
		'''
		pass

	def get_maps(self):
		return self.masterHandler.get_maps(key = 'all')


	### MAIN FUNCTIONS (NON_GAMEPLAY) ###
	'''
	These are the functions that need (not must) to be called by the client
	to run the game
	'''
	def _load_from_dict(self, key2val):
		if key in key2val:
			if key in GAME_ATTR:
				self.GameATTR.add_attr(key, key2val[key])
			elif key in NET_ATTR:
				self.NetATTR.add_attr(key, key2val[key])

		if self.log:
			self.log.add_INFO('World: self attributes set')

	def new_game_from_config(self, path, **kwargs):
		'''
		Load the game from config file
		Args:
			path: path to the config file
		'''
		key2val = read_config_file(path = path, key_list = REQ_GAME_ATTR)
		self._load_from_dict(key2val)

		# if there 

	def new_game(self,
				 username,
				 server_ip,
				 server_port,
				 **kwargs):
		'''
		This function is called to start the new game, the parameters passed through this
		override the ones set using config file.
		
		Args:
			username: username of the bot to register on server
			server_ip: IP address of the server
			server_port: port of the server
			ruleset: ruleset to be used
			topology: 
		'''
		self.new_game_from_config(path = 'default.fccfg', **kwargs)

		# once most of the attributes are loaded we establish the connection
		self.est_conn(username = username, server_ip = server_ip, server_port = server_port)

		self.can_start = True

	def start_game(self):
		# to start the game that has been established
		if self.can_start == True:
			self._start_game()
		else:
			raise ValueError("System not setup for initialization. Kindly check the values!")

		self.is_running = True
		init_state = self.masterHandler.start_game()

		# this function returns the initial map
		return init_state

	def load_saved_game(self, path):
		self.masterHandler.load_saved_game(path)

	def update():
		# check if needed to save game
		if self.GAME_TURN % self.save_game_every == 0:
			self._save_game()

		up_res = masterHandler.update()
		if up_res == 0:
			# game state 0 means the game has ended
			self.is_running = False

		elif up_res == 1:
			print('The network connection dropped (trying again)...')
			self.masterHandler.debug_network()
			print('... Success! Network Connection Re-established.')

	def end_game(save = True):
		# to end the current game and delete the data
		self.is_running = False
		print("end_game() not implemented")


	### MAIN FUNCTIONS (GAMEPLAY) ###
	def get_unit


	# =====================================
	# Non Action Inference Engine Functions
	# =====================================

	def civ_client_status(self):
		# client inference engine
		self.masterHandler.infr_client.show_status()

	def civ_game_status(self):
		# game inference engine
		self.masterHandler.infr_game.show_status()

	def civ_options_status(self):
		# Options inference engine
		self.masterHandler.infr_optns.show_status()

	def civ_rules_status(self):
		# Rules inference engine
		self.masterHandler.infr_rules.show_status()

	## AUXILARY FUNCTIONS ##
	'''
	These are the functions that can be called by the client during gameplay
	'''
	def get_scorecard(plyr_id = None):
		plyr_id = plyr_id or self.plyr_id
		# get scorecard of the player by id
		print("get_scorecard() not implemented")

	def reset():
		# here check state
		# only if it is possible to reset, reset the game
		print("reset() not implemented")

