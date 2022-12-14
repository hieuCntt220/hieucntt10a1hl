Ten = input("Chào bạn, mình là Son, bạn tên là gì: ")
print("Xin Chào",Ten)
#  Code lời chào 

# Tạo biến dùng nhiều --> dễ code
xl = 'Xin lỗi, Son quá vô dụng , thời gian không thể âm được, như tình cảm của Son vậy á'

yn = input('Cùng mình chơi trò chơi nha : Y/N ')   
   #  code câu hỏi bạn có chơi không
   #  Có --> Thực hiện các câu lệnh dưới
   #  Không --> Không thực hiện
   # Nếu như ở trên người dùng chịu chơi trò chơi thì thực hiện còn không thì thực hiện câu lệch (1)    

while yn == "Y" :
    print('Mình có bộ não rất siêu nên mình có thể đổi thời gian: \
        Lựa chọn 1 : Đổi Ngày sang giờ, phút, giây(1) \
            Lựa chọn 2 : Đổi Giây sang phút, giờ, ngày(2)')  
# In ra câu hỏi lựa chọn cho người dùng
    a = input('Hãy nhập lựa chọn của bạn:')
# Người dùng sẽ nhập lựa chọn của mình 



    
    #  Thực hiện điều kiện 1 nếu người dùng lựa chọn 1
    if a == "1" :
        day = float(input('Hãy nhập số ngày bạn mún đổi, Son sẽ trả lời hehe : '))
        if day < 0 :
            # Trả về lỗi khi số tham chiến nhỏ hơn 0
            print(xl)
        else :
            # Tính toán thời gian
            Hours = day*24
            Min = Hours*60
            Sec = Min*60
            print("Vậy", day, "Ngày sẽ bằng" ,Hours,"Giờ", Min,"Phút", Sec,"Giây")    
            lt1 = input("Bạn có mún làm tròn hk, Son sẽ làm tròn cho ạ: C/K ")   
            if lt1 == 'C' : 
                print("Vậy kết quả làm tròn của", day, "Ngày sẽ bằng" ,round(Hours,0),"Giờ", round(Min,0),"Phút", round(Sec,0),"Giây")
                break     
                    
                
    if a == "2": 
        Sec = float(input('Hãy nhập số giây bạn mún đổi, Son sẽ trả lời hehe : '))
        if Sec < 0 :
            print(xl)
        else :
            Min = Sec/60
            Hours = Min/60
            Day = Hours/24
            print("Vậy", Sec, "giây sẽ bằng" , Min,"Phút",Hours ,"Giờ", Day,"Ngày")
            lt2 = input("Bạn có mún làm tròn hk, Son sẽ làm tròn cho ạ: C/K ")   
            if lt2 == 'C' : 
                print("Vậy kết quả làm tròn của", Sec, "giây sẽ bằng" , round(Min,0),"Phút",round(Hours,0) ,"Giờ", round(Day,0),"Ngày")
                break   
yn = input('Bạn có mún tiếp tục nữa hong dợ : Y/N ') 
            # Câu lệnh (1)
if yn == "N" :
    print("Son buồn lắm đó bạn biết hong")

        
      