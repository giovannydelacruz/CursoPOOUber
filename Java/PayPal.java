public class PayPal extends Payment{
    Integer id;
    String email;
    
    public PayPal(Integer id, String email) {
        super(id);
        this.email = email;
    }
}

