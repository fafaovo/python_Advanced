import yagmail

"""
yagamail 发送邮件
1.导入模块
2.使用yagmail创建对象(发件人，发件人授权码，发件的服务器)
3.使用yagmail对象发送邮件(指定收件人，邮件主题，发送的内容)
"""

ya_obj = yagmail.SMTP(user="1016828446@qq.com", password="oufrkrrkxfqcbbjb", host="smtp.qq.com")
content = "这是用python给你发送的一封邮件！\n" \
          "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aspernatur atque, dicta dolores ex illum incidunt labore maxime minus mollitia necessitatibus nulla, odit officia pariatur perspiciatis quis ratione voluptatem! Alias dicta, ex possimus quae quos tempore unde! Alias atque iure libero qui quo. A alias culpa debitis delectus dolorem, eum exercitationem magnam magni non nulla possimus provident qui quisquam quo rem sit tenetur veritatis? Aut blanditiis dolor dolore dolorum fuga illum, inventore ipsam laudantium libero maiores nesciunt officia quod similique sit tempore! Ab consequuntur laudantium molestiae pariatur quidem ullam voluptate? Adipisci quo, reprehenderit? Aspernatur autem facere, iusto modi officiis ut?"
ya_obj.send("zhongzuozhen2017@outlook.com", "测试使用", content)
