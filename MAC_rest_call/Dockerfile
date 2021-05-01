FROM python:3.8

# command to copy MACAddressLookUp.py
ADD MACAddressLookUp.py .

# install dependencie
RUN pip install requests

# command to run on container start
CMD ["python", "./MACAddressLookUp.py"]



