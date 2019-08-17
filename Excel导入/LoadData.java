package com.fh.ks.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

/*导入数据*/

@Entity	//声明实体类
@Table(name="loaddata")	//指定表名
public class LoadData implements java.io.Serializable {//继承了这个接口：可被序列化

	private static final long serialVersionUID = 1L;	
	
	private int id;
	private String name;
	private String age;
	private String sex;
	
	@Id		//主键
	@GeneratedValue //主键标识,自动递增
	@Column(name="id", unique=true, nullable=false)//对应字段名，唯一，非空 ,length=19 指定长度//Column可以不用加，会根据名字匹配
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getAge() {
		return age;
	}
	public void setAge(String age) {
		this.age = age;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	
}
