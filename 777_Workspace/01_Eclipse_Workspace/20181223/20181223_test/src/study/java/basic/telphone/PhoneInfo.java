package study.java.basic.telphone;

public class PhoneInfo {
	String name;
	String phoneNumber;
	String birthday;
	
	public PhoneInfo(String name, String phoneNumber, String birthday) {
		this.name = name;
		this.phoneNumber = phoneNumber;
		this.birthday = birthday;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPhoneNumber() {
		return phoneNumber;
	}
	public void setPhoneNumber(String phoneNumber) {
		this.phoneNumber = phoneNumber;
	}
	public String getBirthday() {
		return birthday;
	}
	public void setBirthday(String birthday) {
		this.birthday = birthday;
	}

	
	public static void main(String[] args) {
		
		PhoneInfo p1 = new PhoneInfo("Ke", "01012341234", "19831127");
		p1.setBirthday("test");
		System.out.println("SSS");
		System.out.println(p1.getBirthday());
	}
}	
	
	