import RPi.GPIO as G
import pushbullet, picamera, time
btn = 2
G.setmode(G.BCM)
G.setup(btn, G.IN)

pb = pushbullet.Pushbullet("o.QQgQh6O6bUqqidXpiBf9VYaQeU40LT1i")

def capture_img(file):
	pc = picamera.PiCamera()
	pc.capture(file)
	pc.close()

def send_img(file):
	f = open(file, "rb")
	image = pb.upload_file(f,file)
	pb.push_file(**image)

ps,count = 1,1

while 1:
	cs = G.input(btn)
	if not ps and cs:
		t = time.time()
		file_name = str(int(t)) + ".jpg"
		capture_img(file_name)
		print("Image Captured")
		send_img(file_name)
		print("Image sent successfully.")
	ps = cs
	time.sleep(0.05)
