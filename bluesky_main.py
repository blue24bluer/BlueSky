import os
import sys
import subprocess
from flask import Flask, render_template, request, Response, jsonify

# تهيئة تطبيق فلاسك وتحديد مسار مجلد القوالب
app = Flask(__name__, template_folder='./Libs/Web')

# المسار الرئيسي الذي يعرض صفحة البحث
@app.route('/')
def index():
    return render_template('bluesky.html')

# المسار الذي يستقبل طلبات البحث
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({"error": "Search query is missing"}), 400

    def generate_output():
        """
        دالة لتشغيل أداة البحث واستقبال النتائج بشكل متدفق.
        تتضمن معالجة آمنة لإنهاء العملية عند انقطاع الاتصال.
        """
        process = None  # تهيئة المتغير
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'Libs', 'Tools', 'BlueSky.py')
            command = [sys.executable, "-u", script_path, '--search', query]

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            # قراءة المخرجات سطرًا بسطر وإرسالها إلى العميل
            for line in process.stdout:
                yield line

        except Exception as e:
            # هذا الاستثناء يحدث عادةً عند إغلاق العميل للاتصال (بالضغط على زر stop)
            # ويعرف باسم BrokenPipeError
            yield f"\n[SERVER-INFO] Connection closed by client. Terminating process.\n"

        finally:
            # ===> التعديل الرئيسي والهام <===
            # هذا الجزء سيعمل دائمًا، سواء انتهى البحث أو تم إيقافه
            if process and process.poll() is None:
                print(f"Terminating process {process.pid}...")
                process.terminate() # إرسال إشارة إنهاء للعملية
                process.wait()      # الانتظار حتى تنتهي بالفعل
                print(f"Process {process.pid} terminated.")


    # إرجاع استجابة متدفقة لعرض النتائج مباشرة في المتصفح
    return Response(generate_output(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
