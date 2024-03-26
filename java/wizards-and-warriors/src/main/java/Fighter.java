class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }

    public String toString() {
        return "Fighter is a " + this.getClass().getSimpleName();
    }
}

class Warrior  extends Fighter{

    @Override
    public String toString() {
        return super.toString();
    }
    @Override
    public boolean isVulnerable() {
        return false;
    }
    @Override
    public int getDamagePoints(Fighter fighter) {
        return fighter.isVulnerable()? 10 : 6;
    }
}

class Wizard  extends Fighter{
    boolean hasSpell;
    Wizard(){
        this.hasSpell = false;
    }
    @Override
    public String toString() {
        return super.toString();
    }
    @Override
    public boolean isVulnerable() {
        return !hasSpell;
    }
    @Override
    public int getDamagePoints(Fighter fighter) {
        return this.hasSpell ? 12 : 3;
    }

    public void prepareSpell(){
        this.hasSpell = true;
    }
}
