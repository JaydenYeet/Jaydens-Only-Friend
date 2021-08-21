from discord.ext import commands

class MyHelp(commands.HelpCommand):
    async def send_client_help(self, mapping):
        channel = self.get_destination()
        await channel.send("hey")

class Help(commands.Cog):
    def __init__(self, client):
       self.client = client
       help_command = MyHelp()
       help_command.cog = self
       client.help_command = help_command

def setup(client):
    client.add_cog(Help(client))