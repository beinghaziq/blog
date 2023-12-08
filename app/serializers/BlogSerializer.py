# import inspect
from app.serializers.UserSerializer import UserSerializer
from pydantic import BaseModel



class BlogSerializer(BaseModel):
    title: str
    body: str
    creator: UserSerializer

# Info: Did some meta programming to pass custom methods along with model attributes.
# custom methods should start with property_ and it will be called dynamically 
#     def property_test(self):
#       return f"Blog title is {self.title}"

#     def to_json(self):
#       data = self.dict()
#       custom_methods = [name for name, _ in inspect.getmembers(self, inspect.ismethod) if name.startswith('property')]
#       for method_name in custom_methods:
#         method = getattr(self, method_name)
#         data[method_name.replace('property_', '')] = method()
#       return data

# To call seralizer with custom methods you'll have to call serailzier as below
# # BlogSerializer(title = blog.title, body = None, creator=blog.creator.__dict__).to_json()
# Will move this code to base seralizer in future
