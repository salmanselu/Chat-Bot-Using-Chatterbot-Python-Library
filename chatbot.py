from chatterbot import ChatBot
import chatterbot
from chatterbot.trainers import ListTrainer
bot = ChatBot(name = 'Unni',
            read_only = True     
            logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch']
             )