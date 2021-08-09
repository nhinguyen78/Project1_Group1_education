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

