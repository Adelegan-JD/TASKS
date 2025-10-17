# Import necessary modules and libraries
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv
import uvicorn
import os
load_dotenv()

# creating an instance for fastapi
app = FastAPI(title= 'My Second FastAPI App', decription= 'This is my second FastAPI app', version= '1.0.0')

# create a data dictionary or the file to display
data = [{"name": "Adelegan Deborah",  "age": 32, "track": "AI Engineering"}, 
{"name": "Adelegan Abigail",  "age": 20, "track": "Blockchain Developer"},
{"name": "Adelegan Esther",  "age": 22, "track": "3D Specialist"}]


# create a validation for the response type expected
class item(BaseModel):
    name: str = Field (..., examples= 'Deborah')        # The "..." makes each field required
    age: int = Field(..., examples = 23)
    track: str = Field(..., examples= 'Developer')

class Update_item(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    track: Optional[str] = None


# Create an action(patch) to update and give it a desciption for the user to see
@app.patch("/update-data/{id}", description="This is the patch endpoint to update the file")
def update_data(id: int, input: Update_item):   # the "input makes sure the required fields are filled with the appropriate input type"       
    updated_file = data[id].update(input.model_dump(exclude_unset=True))           # this passes the incoming input into the already-existing data dictionary
    print(updated_file)
    return {'Message': 'Data Updated', 'Data': data}

# Another method(which can be used for unstructured data) will be to create an empty dictionary and update the empty dictionary with whatever the user inputs. 
# However, this will not involve validation so any other field can be added such that the user can add extra information asides from the fields originally indicated.

# Create the delete action
@app.delete("/remove-data/{id}")
def delete_data(id: int):
    data.remove(data[id])
    return {'Message': 'Data Removed', 'Data': data}


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))       #type:ignore

