import java.util.List;
public class TestTrack {

    public static void race(RemoteControlCar car) {
        // throw new UnsupportedOperationException("Please implement the (static) TestTrack.race() method");
        car.drive();
    }

    /** sort the cars in descending order of number of victories
     * <p>
     * 在Java中，
     * 如果你在一个成员（比如方法或字段）的签名中
     * 使用了一个比该成员可见性低的类，
     * 这通常不是一个问题，因为这样的成员仍然可以在其定义的类的可见性范围内使用。
     * 然而，这可能会导致一些潜在的问题，
     * 尤其是当你尝试在定义类的可见性范围之外使用这些成员时。
     * 例如，在你提供的代码中：
     * <pre>
     * public class Parent {
     *     public Child getChild() {
     *         return new Child();
     *     }
     *     private class Child {}
     * }
     * </pre>
     * Parent 类有一个公共方法 getChild()，它返回一个 Child 类型的对象。
     * 但是，Child 类被定义为私有的（private class Child），
     * 这意味着它只能在 Parent 类的内部被访问。
     * 这可能导致外部代码无法正确使用 getChild() 方法，
     * 因为它无法访问 Child 类型的对象。
     * <b>为了修复这个问题，你需要确保类的可见性至少与其使用者的可见性相同。
     * 在这种情况下，如果你希望 getChild() 方法可以被外部代码使用，
     * 那么 Child 类也应该是公共的（public class Child）
     * 或者至少是包私有的（没有修饰符，默认可见性），
     * 这样它就可以在 Parent 类所在的包中被访问。</b>
     * <hr>
     * <em>如果你正在使用Java 9或更高版本，
     * 并且你的问题是由于模块化导致的，
     * 那么你需要确保引用的类所在的包被导出（exported），
     * 这样其他模块才能访问这些类。
     * 你可以在模块的 module-info.java 文件中使用 exports 关键字来导出包。
     * </em>
     * <hr>
     * </p>
     * <p>在这里我的做法是为  <b>ProductionRemoteControlCar class</b>
     * 添加 public 修饰符、这样它就
     * 不会提示 Class 'ProductionRemoteControlCar' is exposed outside its defined visibility scope </p>
     *
     * @param cars List of cars
     * @return the cars passed in, sorted in descending order of number of victories.
     *
     */
    public static List<ProductionRemoteControlCar> getRankedCars(List<ProductionRemoteControlCar> cars) {
        cars.sort(ProductionRemoteControlCar::compareTo);
        return cars;
    }
}
