python -m venv venv
call venv\Scripts\activate
call pip install -r requirements.txt
call pyinstaller --onefile --name convert-video convert_video.py
call pyinstaller --onefile --name cut-video cut_video.py
call pyinstaller --onefile --name make-gif make_gif.py
call pyinstaller --onefile --name remove-audio remove_audio.py
call pyinstaller --onefile --name resize-video resize_video.py
call pyinstaller --onefile --name slow-motion-correct slow_motion_correct.py
call pyinstaller --onefile --name sort-media sort_media.py