import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
tree = client.tree
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
@client.command()
async def request( ctx):
        embed = discord.Embed(title="Request", description="Click the button below to request", color=discord.Color.green())
        embed.set_footer(text=f"Created_By: {ctx.author.name}")
        await ctx.send(embed=embed, view=test.Request())
class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @commands.Cog.listener() 
    async def on_ready(self):
        print(f"BOT LOGGED AS {self.client.user}")

    #-----Modal----
    class RequestModal(discord.ui.Modal):
        def __init__(self):
            super().__init__(timeout=None, title="Request Form")

        name = discord.ui.TextInput(label="Name", placeholder="Enter your name", style=discord.TextStyle.short)
        age = discord.ui.TextInput(label="Age", placeholder="Enter your age", style=discord.TextStyle.short)
        hobby = discord.ui.TextInput(label="Hobby", placeholder="Enter your hobby", style=discord.TextStyle.short)

        async def on_submit(self, interaction: discord.Interaction):
            channel_id = 1215708476093890600
            channel = interaction.guild.get_channel(channel_id)

            embed = discord.Embed(title=f"{interaction.user.name} Request Form", description=f"**Name**\n{self.name}\n**Age**\n{self.age}", color=discord.Color.green())
            embed.set_footer(text=f"Requested-by:<{interaction.user.id}>")

            await channel.send(embed=embed, view=test.deside_view())
            await interaction.response.send_message("Request Form Submitted", ephemeral=True)

    #---------------
    #-----btns-------
    class deside_view(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
        async def _acc(self, interaction: discord.Interaction, button: discord.ui.Button):
            id = interaction.message.embeds[0].footer.text.split(":")[1].strip()
            channel = interaction.guild.get_channel(1215708476093890600) # ACC CHANNEL
            await channel.send(f"<@{id}> has been accepted")

        @discord.ui.button(label="Decline", style=discord.ButtonStyle.green)
        async def _decline(self, interaction: discord.Interaction, button: discord.ui.Button):
            id = interaction.message.embeds[0].footer.text.split(":")[1].strip()
            channel = interaction.guild.get_channel(1215708476093890600) # DEC CHANNEL
            await channel.send(f"<@{id}> has been declined")

    class Request(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="Request", style=discord.ButtonStyle.green, custom_id="btn-request")
        async def _request(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_modal(test.RequestModal())

#----------------

client.add_cog(test(client))
    

client.run("MTIxNjg2NDA4MDU0ODA3MzYzMw.GY_WjV.ZqQyepCO3rj_kCE1hfuzLTmR1rD23r2nt5kA0g")
