<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ include file="../tool/sessionCheck.jsp"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib prefix="s" uri="/struts-tags" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'lead_data.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

  </head>
  
  <body>  
    <form id="form1" name="form1" action="admin/roleFileUpload.action" method="post" enctype="multipart/form-data">  
        <div align="center" id="div1" style="width: 80%">  
    <table width="80%" border="0" align="center" class="DB_table">  
      <tr bgcolor="#DFF8FF">  
        <td colspan="99" align="left">文件上传</td>  
      </tr>  
      <tr bgcolor="#DFFFBF">  
        <td colspan="99" id="more">
        	文件位置 
          <input type="file" name="uploadFile" size="80"/>  
        </td>  
      </tr>  
      <tr bgcolor="#DFFFBF">  
        <td colspan="99" align="right">
        <input type="submit" value="上传"/>
        <input type="reset" value="重置"/>
        </td>  
      </tr>  
        </table>  
    </div>  
    </form>  
  </body>  

</html>
