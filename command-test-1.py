import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # 1-dimensional list representing the 3x3 board
        self.current_player = 'X' # The player who is currently up to move ('X' or 'O')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        # Check rows, columns and diagonals for a winning line
        lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return self.board[line[0]]
        return None

games = {}

@bot.command()
async def tictactoe(ctx, position: int):
    if ctx.channel.id not in games:
        games[ctx.channel.id] = TicTacToe()
    game = games[ctx.channel.id]
    if game.make_move(position):
        winner = game.check_winner()
        if winner:
            await ctx.send(f'Player {winner} wins!')
            del games[ctx.channel.id] # Delete the game now that it's over
        else:
            await ctx.send(f'Current board: {game.board}')
    else:
        await ctx.send('Invalid move.')

bot.run('token')
