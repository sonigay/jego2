import discord
import asyncio
import random
import os
import datetime
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('jego-972d19158581.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM')



client = discord.Client()



@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="재고현황 ", type=1), afk=False)




@client.event
async def on_message(message):
	global gc #정산
	global creds	#정산
	
# 재고조회안되는 채널 KR1 / KR2 / KR3 / KR5 / KR6 / KRb / KRd   	
	if message.content.startswith('!재고'):
		if message.channel.id == (689426210601959475) or message.channel.id != (689427184443588632) or message.channel.id != (689427209018015842) or message.channel.id != (689427243008655360) or message.channel.id != (689427387859206168) or message.channel.id != (688654225286234146) or message.channel.id != (689426260484423741):
			embed = discord.Embed(
				title='',
				description='```fix\n' + message.author.display_name + '님 안녕하세요!😊\n해당기능은 점검중입니다.\n오류해결후에 다시 찾아뵙도록 하겠습니다.\n\n그동안은 불편하지만 담당영업사원 문의 부탁드립니다. 감사합니다.```',
				color=0xff00ff
				)
			await message.channel.send(embed=embed)	
	
	
	
	
# 재고조회안되는 채널 KR1 / KR2 / KR3 / KR5 / KR6 / KRb / KRd   	
	if message.content.startswith('!재고'):
		if message.channel.id != (689426210601959475) and message.channel.id != (689427184443588632) and message.channel.id != (689427209018015842) and message.channel.id != (689427243008655360) and message.channel.id != (689427387859206168) and message.channel.id != (688654225286234146) and message.channel.id != (689426260484423741):
			embed = discord.Embed(
				title='',
				description='```fix\n' + message.author.display_name + '님 안녕하세요!😊\n요청하신 재고 조회중입니다.\n잠시만 기다려주시기 바랍니다...```',
				color=0xff00ff
				)
			await message.channel.send(embed=embed)	
    

	if message.content.startswith('!재고'):
		if message.channel.id != (689426210601959475) and message.channel.id != (689427184443588632) and message.channel.id != (689427209018015842) and message.channel.id != (689427243008655360) and message.channel.id != (689427387859206168) and message.channel.id != (688654225286234146) and message.channel.id != (689426260484423741):
			SearchID = message.content[len('!재고')+1:]
			await message.channel.send('```fix\n' + SearchID + ' 재고 선택중...```')
			gc = gspread.authorize(creds)
			wks = gc.open('재고관리').worksheet('구단위코드/재고출력')
	
			wkstime = gc.open('재고관리').worksheet('재고데이터')
			wks.update_acell('A1', SearchID)
			await message.channel.send('```fix\n' + SearchID + ' 재고 조회중...```')
			result = wks.acell('B1').value
			result2 = wkstime.acell('A1').value
			await message.channel.send("```fix\n마지막 업로드시간 확인중...```")
			result3 = wks.acell('c1').value
			result4 = wks.acell('d1').value
			
			embed1 = discord.Embed(
				title = ' :calling:  ' + SearchID + ' 재고현황! ',
				description= '**```css\n' + SearchID + ' 재고현황 입니다.\n마지막 데이터 업로드시간은\n'+ result2 + ' 입니다.' + result + '```**',
				color=0xff00ff
				)
			embed3 = discord.Embed(
				title = '',
				description= '**```css\n' + result3 + '```**',
				color=0xff00ff
				)
			embed4 = discord.Embed(
				title = '',
				description= '**```css\n' + result4 + '실시간조회가 아니라서 다소 차이가 있을수 있습니다. ```**',
				color=0xff00ff
				)		
			embed2 = discord.Embed(
				title = ' :calling: ' + SearchID + ' 재고조회!! ',
				description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
				color=0xff00ff
				)
			await message.channel.send('```fix\n' + SearchID + ' 재고현황 출력중...```')
			await message.channel.send(embed=embed1)
			await message.channel.send(embed=embed3)
			await message.channel.send(embed=embed4)
			await client.get_channel(674838122332291082).send(embed=embed2)
		
	if message.content.startswith('!모델명'):
		embed = discord.Embed(
			title='',
			description='```fix\n' + message.author.display_name + '님 안녕하세요!😊\n요청하신 모델명 출력중입니다.\n잠시만 기다려주시기 바랍니다...```',
			color=0x0000ff
			)
		await message.channel.send(embed=embed)	
            
	if message.content.startswith('!모델명'):
		SearchID = message.content[len('!모델명')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('재고관리').worksheet('모델명출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed = discord.Embed(
			title = ' :printer:  모델명 코드 리스트 ',
			description= '**```css\n' + SearchID + ' 모델명 코드는 ' + result + '```**',
			color=0x0000ff
			)
		await message.channel.send(embed=embed)
                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
