//
// This is only a SKELETON file for the 'Bank Account' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class BankAccount {
    #balance=0;
    #accountState=null;
    constructor() {}

    open() {
        if (this.#accountState==true){
            throw new ValueError;
        }else{
            this.#balance=0;
            this.#accountState=true;
        }
    }

    close() {
        if([false,null].includes(this.#accountState)){
            throw new ValueError;
        }
        this.#accountState=false;
    }

    deposit(num) {
        this.handle_account({num:num, hand:"deposit"});
    }

    withdraw(num) {
        this.handle_account({num:num, hand:"withdraw"});
    }

    get balance() {
        if (this.#accountState==true){
            return this.#balance
        }else{
            throw new ValueError;
        }
    }

    handle_account(option){
        if (this.#accountState==false || option.num<0){
            throw new ValueError;
        }else if (option.hand == "withdraw"  && this.#accountState==true){
            let tmp_balance=this.#balance-option.num;
            if(tmp_balance<0){
                throw new ValueError;
            }
            this.#balance=tmp_balance;
        }else if(option.hand=='deposit' && this.#accountState==true){
            this.#balance+=option.num;
        }
    }
}

export class ValueError extends Error {

    constructor() {
        super('Bank account error');
    }

}
