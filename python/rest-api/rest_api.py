import json


class RestAPI:
    def __init__(self, database=None):
        self.db=database
        
    def get(self, url, payload=None):
        if url=="/users":
            return json.dumps({"users":[user for user in self.db["users"] if user["name"] in json.loads(payload)["users"]]})

    def post(self, url, payload=None):
        if url=="/add":
            return json.dumps({"name": json.loads(payload)["user"], "owes": {}, "owed_by": {}, "balance": 0.0})
        
        elif url=="/iou":
            payload_py=json.loads(payload)
            lender,borrower,mount=payload_py["lender"],payload_py["borrower"],payload_py["amount"]
            iou_info=filter(lambda x:x['name'] in [lender,borrower],self.db['users'])
            
            for iou in iou_info:
                if iou["name"]==lender and borrower in iou['owes']:
                    if mount<=iou['owes'][borrower]:
                        iou['owes'][borrower]-=mount
                        if not iou['owes'][borrower]:
                            del iou['owes'][borrower]
                    else:
                        iou['owed_by'][borrower]=mount-iou['owes'][borrower]
                        del iou['owes'][borrower]
                        
                    iou["balance"]+=mount
                        
                elif iou['name']==borrower and lender in iou['owed_by']:
                    if mount<=iou['owed_by'][lender]:
                        iou['owed_by'][lender] -=mount
                        if not iou['owed_by'][lender]:
                            del iou['owed_by'][lender]
                        
                    else:
                        iou['owes'][lender]=mount-iou['owed_by'][lender]
                        del iou['owed_by'][lender]
                    
                    iou["balance"]-=mount
                    
                elif iou["name"]==lender and borrower not in iou['owes']:
                    borr=iou['owed_by']
                    borr[borrower]=borr.get(borrower,0)+mount
                    iou["balance"]+=mount
                    
                elif iou['name']==borrower and lender not in iou['owed_by']:
                    lend=iou['owes']
                    lend[lender]=lend.get(lender,0)+mount
                    iou["balance"]-=mount
                    

            new_iou={"users":[user for user in self.db["users"] if user['name'] in [lender,borrower]]}
            return json.dumps(new_iou)
