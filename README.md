
# Auto Zoom Participation and Grader

Instructors can track Zoom participation and submit grades directly to Canvas

## Installation

create python virtual envirnment and install dependences
```bash
  # Linux
  python3 -m venv env
  source env/bin/activate

  # Windows
  py -m venv env
  .\env\Scripts\activate
```
```bash
  cd 
  pip install -r requirements.txt
  
```

    
## Environment Variables

To run this project, you will need to add the following environment variables to submit_to_canvas.py

generate your Canvas API key and add to  
```API_TOKEN = ''```    
[Instructions for generating Canvas API Token](https://kb.iu.edu/d/aaja)

add course id to    
```course_id = ''```


## Run Locally

Parce a Zoom Chat

```bash
  python parcer.py <path to file>
```

Submit grades from CSV file
```bash
python submit_to_canvas.py <path to file>
```



## Contributing

Improvments that can be made

TODO:
- currenlty the parce zoom chat and the submit grade to canvas are two seperate functinalities. Integrate a way to bundle those toghter so that once one file is parced the request to update grades is sent automatically
- currenlty the assignment id needs to be manully added to the csv file. Implemnet a way to fetch the assignmet ids.


