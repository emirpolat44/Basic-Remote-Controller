import random
import time

class RemoteControl():
    def __init__(self,tv_Status = "OFF",tv_Volume = 0,tv_ChannelList = ["TRT"],tv_Channel = "TRT"):
        self.tv_Status = tv_Status
        self.tv_Volume = tv_Volume
        self.tv_ChannelList = tv_ChannelList
        self.tv_Channel = tv_Channel

    def tv_TurnOn(self):
        if (self.tv_Status == "ON"):
            print("the TV is already ON")
        else:
            print("the TV is turning ON")
            self.tv_Status = "ON"

    def tv_TurnOff(self):
        if (self.tv_Status == "OFF"):
            print("the TV is already OFF")
        else:
            print("the TV is turning OFF")
            self.tv_Status = "OFF"

    def tv_adjustVolume(self):
        while True:
            vol = input("Increase volume '>'\nReduce volume '<'\nExit '0'\n:")
            if(vol == "<"):
                if (self.tv_Volume != 0):
                    amount = int(input("Enter the amount to reduce the volume: "))
                    self.tv_Volume -= amount
                    print("Volume :",self.tv_Volume)
            elif (vol == ">"):
                if (self.tv_Volume != 100):
                    amount = int(input("Enter the amount to increase the volume: "))
                    self.tv_Volume += amount
                    print("Volume :", self.tv_Volume)
            else:
                print("Volume Changed :",self.tv_Volume)
                break

    def tv_ChannelAdd(self,channel_Name):
        print("Adding Channel")
        time.sleep(1)
        self.tv_ChannelList.append(channel_Name)
        print("Channel Added")

    def random_Channel(self):
        randomChannel = random.randint(0,len(self.tv_ChannelList)-1)
        self.tv_Channel = self.tv_ChannelList[randomChannel]
        print("Current Channel :", self.tv_Channel)

    def __len__(self):
        return len(self.tv_ChannelList)

    def __str__(self):
        return "TV Status :{}\nTV Channel :{}\nTV Volume :{}\nTV Channel List :{}".format(self.tv_Status,self.tv_Channel,self.tv_Volume,self.tv_ChannelList)

RC = RemoteControl()

print("-" * 20
      + "\n -1- Turn on TV\n"
      + " -2- Turn off TV\n"
      + " -3- Volume Settings\n"
      + " -4- Add Channel\n"
      + " -5- Number of Channels\n"
      + " -6- Random Channel\n"
      + " -7- TV Status\n"
      + "to Exit 'exit'\n"
      + "-" * 20)

while True:
    option = input("\nPlease, Choose from the following options :")
    if (option == "exit"):
        break
    elif (option == "1"):
        RC.tv_TurnOn()
        continue
    elif (option == "2"):
        RC.tv_TurnOff()
        continue
    elif (option == "3"):
        RC.tv_adjustVolume()
        continue
    elif (option == "4"):
        channel = input("New Channel Name :")
        RC.tv_ChannelAdd(channel)
        continue
    elif (option == "5"):
        print(RC.__len__())
        continue
    elif (option == "6"):
        RC.random_Channel()
        continue
    elif (option == "7"):
        print(RC)
        continue