package com.fh.ks.action;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletResponse;

import org.apache.commons.io.FileUtils;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.struts2.ServletActionContext;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import com.fh.ks.model.LoadData;
import com.opensymphony.xwork2.ActionSupport;

@Component("roleFileAction")	// 注入spring
@Scope("prototype")
public class RoleFileUploadAction extends ActionSupport {
	
	private static final long serialVersionUID = 1L;
	private File uploadFile;
	private String uploadFileFileName;					//文件名



	@Override
	public void validate() {
		super.validate();
	}

	//go页面
	public String goLoadPage(){
		return SUCCESS;
	}

	public String loadRoleFile() {

		String directory = "/upload/role";
		String targetDirectory = ServletActionContext.getServletContext().getRealPath(directory);	//设定上传路径
		
		//System.out.println("-------"+uploadFileFileName);
		
		// 生成上传的文件对象
		File target = new File(targetDirectory, uploadFileFileName);
		// 如果文件已经存在，则删除原有文件
		if (target.exists()) {
			target.delete();
		}
		// 复制file对象，实现上传
		try {
			FileUtils.copyFile(uploadFile, target);

			// out = response.getWriter();
			// out.print("文件上传成功！");
		} catch (IOException e) {
			e.printStackTrace();
		}

		loadRoleInfo(uploadFileFileName);									//---------------------------------------------------------------------
		return SUCCESS;
	}

	/**
	 * 把Excele表读出的数据，组装成一个List,统一导入数据库
	 * 
	 * @param uploadFileFileName
	 */
	public void loadRoleInfo(String uploadFileFileName) {

		String directory = "/upload/role";
		String targetDirectory = ServletActionContext.getServletContext().getRealPath(directory);
		File target = new File(targetDirectory, uploadFileFileName);

		List<LoadData> roleList = new ArrayList<LoadData>();
		try {
			FileInputStream fi = new FileInputStream(target);
			Workbook wb = new HSSFWorkbook(fi);
			
			Sheet sheet = wb.getSheetAt(0);								//第一个sheet

			int rowNum = sheet.getLastRowNum() + 1;						//取得最后一行的行号
			for (int i = 1; i < rowNum; i++) {
				LoadData ptRoleInfo = new LoadData();
				Row row = sheet.getRow(i);								//行
				int cellNum = row.getLastCellNum();						//每行的最后一个单元格里的数据									
				for (int j = 0; j < cellNum; j++){
					Cell cell = row.getCell(j);
					String cellValue = null;
					switch (cell.getCellType()) { 						// 判断excel单元格内容的格式，并对其进行转换，以便插入数据库
					case 0:
						cellValue = String.valueOf((int) cell.getNumericCellValue());
						break;
					case 1:
						cellValue = cell.getStringCellValue();
						break;
					case 2:
						cellValue = cell.getNumericCellValue() + "";
						//cellValue = String.valueOf(cell.getDateCellValue());
						break;
					case 3:
						cellValue = "";
						break;
					case 4:
						cellValue = String.valueOf(cell.getBooleanCellValue());
						break;
					case 5:
						cellValue = String.valueOf(cell.getErrorCellValue());
						break;
					}

					switch (j) {// 通过列数来判断对应插如的字段
					case 0:
						//ptRoleInfo.setId(Integer.parseInt(cellValue));
						ptRoleInfo.setId(1);
						break;
					case 1:
						ptRoleInfo.setName(cellValue);
						break;
					case 2:
						ptRoleInfo.setAge(cellValue);
						break;
					case 3:
						ptRoleInfo.setSex(cellValue);
						break;
					}
				}
				roleList.add(ptRoleInfo);
			}
			
			//fileLoadDao.roleInfotoDB(roleList);
			for(int n=0; n<roleList.size(); n++){
				LoadData ld = roleList.get(n);
				System.out.println(ld.getId()+"---"+ld.getName()+"---"+ld.getAge()+"---"+ld.getSex());
			}
			//System.out.println("---"+roleList);
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public File getUploadFile() {
		return uploadFile;
	}

	public void setUploadFile(File uploadFile) {
		this.uploadFile = uploadFile;
	}

	public String getUploadFileFileName() {
		return uploadFileFileName;
	}

	public void setUploadFileFileName(String uploadFileFileName) {
		this.uploadFileFileName = uploadFileFileName;
	}

}
