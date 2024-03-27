class Badge {
    public String print(Integer id, String name, String department) {
        // throw new UnsupportedOperationException("Please implement the Badge.print() method");
        String localId = id == null ? "" : "["+ id + "] - ";
        String localDepartment = department == null ? " - OWNER" : " - " + department.toUpperCase();
        String label = localId +  name + localDepartment;
        return label.trim();
    }
}
