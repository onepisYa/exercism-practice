import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class AppointmentScheduler {

    private  LocalDateTime  appointmentDateTime;
    public LocalDateTime schedule(String appointmentDateDescription) {
        DateTimeFormatter parser = DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss");
        return LocalDateTime.parse(appointmentDateDescription, parser);
    }

    public boolean hasPassed(LocalDateTime appointmentDate) {
        // return this.appointmentDateTime.isAfter(appointmentDate);
         return LocalDateTime.now().isAfter(appointmentDate);
    }

    public boolean isAfternoonAppointment(LocalDateTime appointmentDate) {
        return appointmentDate.getHour() >= 12 && appointmentDate.getHour() < 18;
    }

    public String getDescription(LocalDateTime appointmentDate) {
        DateTimeFormatter datePrinter = DateTimeFormatter.ofPattern("EEEE, MMMM d, yyyy, ");
        DateTimeFormatter timePrinter = DateTimeFormatter.ofPattern("h:mm a.");
        return "You have an appointment on " + datePrinter.format(appointmentDate) + "at " + timePrinter.format(appointmentDate);

    }

    public LocalDate getAnniversaryDate() {
        // returns this year's anniversary date, which is September 15th
        return LocalDate.of(LocalDate.now().getYear(), 9, 15);
    }
}
