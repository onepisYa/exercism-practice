class AnnalynsInfiltration {

    /**
     * <h1> Check if a fast attack can be made. </h1>
     * <p>
     * Fast attack: a fast attack can be made if the knight is sleeping,
     * as it takes time for him to get his armor on, so he will be vulnerable.
     * </p>
     */
    public static boolean canFastAttack(boolean knightIsAwake) {
        // throw new UnsupportedOperationException("Please implement the (static) AnnalynsInfiltration.canFastAttack() method");
        return !knightIsAwake;
    }

    /**
     * <h1>Check if the group can be spied upon</h1>
     * <p>Spy: the group can be spied upon if at least one of them is awake.
     * Otherwise, spying is a waste of time.</p>
     */
    public static boolean canSpy(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake) {
        // throw new UnsupportedOperationException("Please implement the (static) AnnalynsInfiltration.canSpy() method");
        return knightIsAwake || archerIsAwake || prisonerIsAwake;
    }

    /**
     * <h1>Check if the prisoner can be signalled</h1>
     *<p>Signal prisoner:
     * the prisoner can be signalled using bird sounds
     * if the prisoner is awake and the archer is sleeping,
     * as archers are trained in bird signaling, so they could intercept the message.</p>
     */
    public static boolean canSignalPrisoner(boolean archerIsAwake, boolean prisonerIsAwake) {
        // throw new UnsupportedOperationException("Please implement the (static) AnnalynsInfiltration.canSignalPrisoner() method");
         return prisonerIsAwake && !archerIsAwake;
    }

    /**
     * <h1>Check if the prisoner can be freed</h1>
     * <p>Free prisoner: Annalyn can try sneaking into the camp to free the prisoner.</p>
     * <p>
     * This is a risky thing to do and can only succeed in one of two ways:
     * <li>If Annalyn has her pet dog with her she can rescue the prisoner if the archer is asleep.</li>
     *      <ul><li>The knight is scared of the dog and the archer will not have time to get ready before Annalyn and the prisoner can escape.</li></ul>
     * <li>If Annalyn does not have her dog then she and the prisoner must be very sneaky!</li>
     * </p>
     */
    public static boolean canFreePrisoner(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake, boolean petDogIsPresent) {
        // throw new UnsupportedOperationException("Please implement the (static) AnnalynsInfiltration.canFreePrisoner() method");

        // petDogIsPresent && !archerIsAwake; can be free
        // !archerIsAwake && !knightIsAwake && prisonerIsAwake; can be free
        return petDogIsPresent && !archerIsAwake  || !archerIsAwake && !knightIsAwake && prisonerIsAwake;
    }
}
