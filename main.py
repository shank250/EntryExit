# import cv2
# # from pyzbar import pyzbar
# # import glob 
# import time
# # import pandas as pd
# # import pathlib
# import json
# # url = 'http://192.168.13.67:4747/video'
# url = 'http://192.0.0.4:8080/video'
# # in_room = []
# # counter = 0

# def decode_qr_codes():
#     cap = cv2.VideoCapture(url)

#     while True:
#         ret, frame = cap.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         detect = cv2.QRCodeDetector()
#         value, points, straight_qrcode = detect.detectAndDecode(gray)

#         if value :
#             # print(f"Data: {value}")
#             spliting = value.split("id=")
#             global id
#             id = spliting[1]
#             print("ID : ",id)
#             break
#         # cv2.imshow("QR Code Scanner", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()


# # def in_out():
# #     if len(in_room) < 1 :
# #         no_of_people = f"No of people in the room : {len(in_room)} \nStatus : Enter" 
# #         return no_of_people 
# #     else :
# #         no_of_people = f"No of people in the room : {len(in_room)} \nStatus : Wait" 
# #         return no_of_people 
    

# # id = "AIMLFW2201"
# def search():
#     with open("data.json", 'r+') as file:
#         data = json.load(file)
#     with open("registered_cand.json", 'r') as file:
#         reg_data = json.load(file)

#     def linear_search(strings, target):
#         for string in strings:
#             if string == target:
#                 return True
#         return False
#     # status = " "
#     # if id in in_room :
#     #     in_room.remove(id)
#     #     status = "Status : Exit"
#     #     print(status)
#     #     main()

#     # print(id)
#     if linear_search(reg_data["reg_id"], id):
#         print( "DETAILS : Registered \n")
#         # in_room.append(id)
#         time.sleep(3)
#         print("scanning...")
#     else:
#         print( "DETAILS : Unregistered")
#         if linear_search(data["id"], id):
#             print( "STATUS : Re-entry denied")
#         else:
#             print( "DETAILS : New candidate \nSTATUS : Enter")
#             id_list = data["id"]
#             # in_room.append(id)
#             id_list.append(id)  
#             data["id"] = id_list
#             with open("data.json", 'w') as file:
#                 json.dump(data, file) #, indent=4
#         time.sleep(3)
        
#         # if status != " ":
#         #     print(status)
#         print("scanning...")
#         main()

# def main():
#     while True:
#         decode_qr_codes()
#         search()
# main()
    
# # decode_qr_codes()