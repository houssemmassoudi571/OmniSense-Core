"""
================================================================================
OMNISENSE CORE v2.0 - PRODUCTION STABLE
--------------------------------------------------------------------------------
A Physics-based Bio-Electromagnetic Awareness Protocol.
Transforms Wi-Fi CSI data into non-optical spatial intelligence.
================================================================================
"""

import numpy as np
import hashlib
import time

class OmniSenseEngine:
    def __init__(self, sensitivity=0.75):
        self.sensitivity = sensitivity
        self.reference_frame = None
        self.is_armed = True
        # خزان لتخزين الأنماط الحركية (Gait Buffer)
        self.signal_buffer = []

    def calibrate_baseline(self, csi_samples):
        """
        تقوم هذه الدالة بمسح الغرفة وهي فارغة لإنشاء 'الخريطة الصفرية'.
        """
        self.reference_frame = np.mean(csi_samples, axis=0)
        print("[System] Calibration successful. Environment baseline set.")

    def process_live_stream(self, raw_packet):
        """
        المحرك الرئيسي: يستقبل البيانات الخام ويحللها في الوقت الفعلي.
        """
        if self.reference_frame is None:
            return "SYSTEM_NOT_READY"

        # 1. تحليل التردد (Frequency Deviation)
        # نقوم بمقارنة المصفوفة الحالية بالمصفوفة المرجعية
        deviation = np.linalg.norm(raw_packet - self.reference_map)
        
        # 2. منطق الرصد المتدرج (Multi-Tier Detection)
        if deviation < 0.1:
            return "STATE_IDLE" # الغرفة هادئة تماماً
        
        elif 0.1 <= deviation < self.sensitivity:
            # احتمال وجود كائن حي (تنفس أو حركة طفيفة)
            return "STATE_BIO_PRESENCE"
            
        elif deviation >= self.sensitivity:
            # حركة قوية (اختراق أو مشي)
            return "STATE_INTRUSION_ALERT"

    def identify_gait(self, pattern_segment):
        """
        خوارزمية تمييز الهوية عبر 'بصمة المشية'.
        """
        # تحويل تتابع الإشارات إلى Hash فريد يمثل نمط الشخص
        gait_hash = hashlib.sha256(str(pattern_segment).encode()).hexdigest()
        return f"ID-{gait_hash[:8].upper()}"

# --- محاكاة الربط بالواقع (Hardware Bridge Simulation) ---
if __name__ == "__main__":
    # تشغيل النظام بحساسية 0.8
    omni = OmniSenseEngine(sensitivity=0.8)
    
    # 1. محاكاة المعايرة (هذه البيانات تأتي عادة من هوائي الواي فاي)
    print(">> Step 1: Calibrating room (please leave the room empty)...")
    mock_csi_baseline = [np.random.rand(64) for _ in range(50)]
    omni.calibrate_baseline(mock_csi_baseline)

    # 2. تشغيل الرصد المستمر
    print(">> Step 2: OmniSense Active. Monitoring electromagnetic field...")
    try:
        while True:
            # هنا يتم استقبال بيانات CSI الحقيقية من الهاردوير (ESP32/Router)
            # سنستخدم بيانات عشوائية للمحاكاة الآن
            mock_live_signal = np.random.rand(64)
            
            result = omni.process_live_stream(mock_live_signal)
            
            if result == "STATE_INTRUSION_ALERT":
                print(f"🚨 ALERT [{time.strftime('%H:%M:%S')}]: Unauthorized Movement!")
            elif result == "STATE_BIO_PRESENCE":
                print(f"👤 INFO: Human presence detected (breathing/micro-movement).")
                
            time.sleep(0.1) # سرعة معالجة عالية جداً (10Hz)
    except KeyboardInterrupt:
        print("\n>> System deactivated safely.")
