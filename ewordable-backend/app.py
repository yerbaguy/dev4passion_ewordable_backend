from flask import Flask, jsonify
from youtube_transcript_api import YouTubeTranscriptApi as yta
from textblob import TextBlob
import numpy as np

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_articles():
 return jsonify({"Hello":"World"})

@app.route('/get_better_captionss', methods = ['GET'])
def get_better_captionss():
    vid_id = "As3TT3xlddU&t=558s"
    data = yta.get_transcript(vid_id)
    transcript = ''

    for value in data:
        for key, val in value.items():
            if key == 'text':
               transcript += val

    outPut = transcript.splitlines()
    final_output = ''.join(outPut)

   #print_type
   # print(type(final_output))

    x:string = final_output


    #worked
    text = "The titular threat of The Blob has always struck me as the ultimate movie "
    
    #text = text.read()
    #array_string = np.array(final_output)
    #blob = TextBlob(array_string)

    #worked
    # blob = TextBlob(text)
    blob = TextBlob(x)

    #worked
    return blob.words
 
# return text


    #b = str("Machin Learnin")
    #x = TextBlob(b)
    #return x.correct()
    
    #return b.tags



@app.route('/get_better_captions', methods = ['GET'])
def get_better_captions():
    vid_id = "As3TT3xlddU&t=558s"
    data = yta.get_transcript(vid_id)
    transcript = ''

    for value in data:
        for key, val in value.items():
            if key == 'text':
               transcript += val

    outPut = transcript.splitlines()
    final_output = ''.join(outPut)
    #return final_output
    x = str(final_output)
    #return x

   # b = TextBlob(final_output)
   # return b.correct()
    b = TextBlob(x)
    #return b.correct()
    return TextBlob("")
    


@app.route('/get_captions', methods = ['GET'])
#@app.route('/get_captions'methods = ['GET'])
def get_captions():
    vid_id = "As3TT3xlddU&t=558s"
    data = yta.get_transcript(vid_id)
    transcript = ''

    for value in data:
        for key, val in value.items():
            if key == 'text':
               transcript += val

    outPut = transcript.splitlines() 
    final_output = ''.join(outPut)

#print(final_output)

    return final_output


if __name__ == "__main__":

  # app.run(debug=True)
  # app.run(host='0.0.0.0', port=5000)
  app.run(host='0.0.0.0', port=5000)
