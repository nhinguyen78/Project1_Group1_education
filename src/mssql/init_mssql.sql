-- ****************************************
-- Create Database
-- ****************************************

CREATE DATABASE EducationData;
GO

USE EducationData;
GO

-- ****************************************
-- Create Schema
-- ****************************************

CREATE SCHEMA [ClassQuality] AUTHORIZATION [dbo];
GO

-- ****************************************
-- Create Table
-- ****************************************

USE EducationData
GO

/****** Object:  Table [dbo].[CoursesData] ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[CoursesData](
	[Course_ID] [nvarchar](50) NOT NULL,
	[Course_Name] [nvarchar](50) NOT NULL,
	[Instructor_ID] [nvarchar](50) NOT NULL,
	[Month_Duration] [nvarchar](50) NOT NULL,
	[Price_in] [int] NOT NULL,
	[Online] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_CoursesData] PRIMARY KEY CLUSTERED 
(
	[Course_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[TracsactionData] ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[TracsactionData](
	[Transaction_ID] [nvarchar](50) NOT NULL,
	[Instructor_ID] [nvarchar](50) NOT NULL,
	[Course_ID] [nvarchar](50) NOT NULL,
	[Student_ID] [int] NOT NULL,
	[Date] [datetime2](7) NOT NULL,
 CONSTRAINT [PK_TracsactionData] PRIMARY KEY CLUSTERED 
(
	[Transaction_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[InstructorData] ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[InstructorData](
	[Instructor_ID] [int] NOT NULL,
	[Instructor_Name] [nvarchar](70) NOT NULL,
	[Instructor_email] [nvarchar](50) NOT NULL, 
   	[Instructor_address] [nvarchar](70) NOT NULL,
	[Instructor_PhoneNum] [nvarchar](25) NOT NULL,
	[Instructor_level] [nvarchar](20) NOT NULL,
   	[Total_courses_released] [int] NOT NULL,
    	[Instructor_ranked] [int] NOT NULL,
    	[Gender] [nvarchar](10) NOT NULL,
 CONSTRAINT [PK_InstructorData] PRIMARY KEY CLUSTERED 
(
	[Instructor_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[StudentData] ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[StudentData](
	[Student_ID] [int] NOT NULL,
	[Name] [nvarchar](70) NOT NULL,
	[Gender] [nvarchar](10) NOT NULL, 
   	[DOB] [date] NOT NULL,
    	[Email] [nvarchar](50) NOT NULL,
    	[Address] [nvarchar](70) NOT NULL,
	[PhoneNumber] [nvarchar](25) NOT NULL,
    	[Final_Score] [int] NOT NULL,
    	[Rating_class] [int] NOT NULL,
    	[Rating_teacher] [int] NOT NULL,
    	[Class_recommendation] [nvarchar](5) NOT NULL,
 CONSTRAINT [PK_StudentData] PRIMARY KEY CLUSTERED 
(
	[Student_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

