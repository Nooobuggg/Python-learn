books = {
    
    "python":"Python爬虫从入门到入狱",
    "c":"C语言从0基础到-1基础",
    "java":"Java从代码到泡茶",
    "css":"CSS从编码到美工",
    "c++":"C++从入门到入土"
    
}
books["kali"] = "Kali从入狱到入土"

while True:
    messages = input("输入一个图书名：")
    if messages in books:
        print("你查找的图书是：")
        print("名字：" + messages , "序言：" + books[messages])
    else:
        print("没有此图书")
        print("图书馆有" + str(len(books)) + "本书")
        print("图书列表：")
        for name,num in books.items():
            print("\t" + "名字：" + name , "序言：" + num)
        