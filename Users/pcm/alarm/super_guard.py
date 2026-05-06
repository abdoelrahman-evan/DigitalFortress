import cv2
import json
import winsound  # مكتبة إصدار الأصوات في ويندوز
import time

# 1. تحميل الإعدادات من ملف الـ JSON اللي عملناه
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
    print(f"✅ Configuration Loaded: {config['app_name']} is ready.")
except FileNotFoundError:
    print("❌ Error: config.json not found! Please create it first.")
    exit()

# التأكد من حالة الإنذار الصوتي من الإعدادات
alarm_enabled = config['security']['alarm_sound']

# 2. تشغيل الكاميرا وتجهيز النظام
cap = cv2.VideoCapture(0)
time.sleep(2)  # إعطاء الكاميرا وقت لتضبط الإضاءة

# التقاط أول لقطة للمقارنة (الخلفية الثابتة)
ret, frame1 = cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

print("🛡️ SUPER GUARD ACTIVE: Monitoring for movement...")
if alarm_enabled:
    print("🔊 Audio Alarm: ENABLED")

while True:
    ret, frame2 = cap.read()
    if not ret:
        break

    # معالجة اللقطة الحالية
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # حساب الفرق بين اللقطة الأولى والحالية
    delta = cv2.absdiff(gray1, gray2)
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
    
    # إذا كان التغيير كبيراً (اكتشاف حركة)
    if thresh.sum() > 500000:
        print("⚠️ INTRUDER DETECTED! Taking action...")
        cv2.imwrite('intruder_alert.jpg', frame2)
        
        # إذا كان المستخدم مفعل الصوت في الـ JSON
        if alarm_enabled:
            # إصدار صوت إنذار حاد (التردد: 2500 هرتز، المدة: 1000 مللي ثانية)
            winsound.Beep(2500, 1000) 
        
        break # إنهاء البرنامج بعد تصوير الدخيل

cap.release()
print("🔐 System secured. Check 'intruder_alert.jpg' for evidence.")
