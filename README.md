# liveTwitterSentimentAnalysis
Cách setup project:
1. clone github repository
2. pip install -r requirements.txt
- Warning: khi gõ lệnh pip trên thì các packages trong requirement sẽ được install global, vì vậy nếu muốn chỉ install ở trong project thì phải tạo virtual environment venv.
- Cách làm thì tự search mạng nhé :)) gõ how to create venv in vscode, pycharm... là ra.
- Hoặc cứ install global rồi khi nào xong việc thì gõ lệnh pip uninstall -r requirements.txt để gỡ cài đặt hết mấy cái packages cũng được. Mấy cái packages cũng nhẹ hều à.
3. sau khi setup xong thì chỉ cần gõ lệnh python app.py, chờ khoảng 5p để app chạy xong và vào http://127.0.0.1:5000/ để test app.
4. Nếu sau khi nhập username và số lượng tweet rồi cho chạy mà bị lỗi List Index out of range thì cứ reload lại trang là được.
