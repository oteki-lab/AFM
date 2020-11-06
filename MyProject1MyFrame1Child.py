"""Child class of MyFrame1"""

import os
import csv
import json
import numpy as np
import cv2
import wx
from MyProject1MyFrame1 import MyProject1MyFrame1

class MyProject1MyFrame1Child(MyProject1MyFrame1):
	"""Child class"""
	def __init__(self, parent):
		MyProject1MyFrame1.__init__(self, parent)
		self.path = ''
		self.cmap = ''
		self.output_tif = ''
		self.output_csv = ''
		self.output_json = ''
		self.dots_json = ''
		self.output_dir = ''
		self.img = ''
		self.states = {'marker':True, 'rect':False}
		self.m_checkBox1.SetValue(self.states['marker'])
		self.m_checkBox2.SetValue(self.states['rect'])
		self.params = {
						'blur': 1,
						'threshold': 125,
						'medianBlur': 1,
						'threshold1': 400,
						'threshold2': 1000,
						'dilate': 1,
						'area': 76,
						'height': 10.0
		}
		self.org_img = ''
		self.base_img = ''
		self.m_slider2.SetValue(self.params['blur'])
		self.m_spinCtrl5.SetValue(self.params['threshold'])
		self.m_slider4.SetValue(self.params['medianBlur'])
		self.m_spinCtrl1.SetValue(self.params['threshold1'])
		self.m_spinCtrl2.SetValue(self.params['threshold2'])
		self.m_slider5.SetValue(self.params['dilate'])
		self.m_spinCtrl3.SetValue(self.params['area'])
		self.m_spinCtrlDouble1.SetValue(self.params['height'])
		self.dots = []
		self.row = -1

	@classmethod
	def show_image(cls, img, pannel, resize=0):
		"""Return picture"""
		width, height = pannel.Size
		new_width, new_height = width, height
		if resize == 1:
			new_height = height if width > height else int(img.shape[0]*width/img.shape[1])
			new_width = int(img.shape[1]*height/img.shape[0]) if width > height else width
		img = cv2.resize(img, (new_width, new_height))
		buf = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		bmp = wx.Bitmap.FromBuffer(img.shape[1], img.shape[0], buf)
		wx.StaticBitmap(pannel, wx.ID_ANY, bmp)

	def rendering(self):
		"""Display picture"""
		source = self.m_textCtrl1.GetValue()
		img = cv2.imread(source)

		font = cv2.FONT_HERSHEY_DUPLEX
		color = (0, 255, 0)
		for dot in self.dots:
			if self.states['marker']:
				if dot['marker'] == '1':
					org = (dot['approx'].ravel()[0], dot['approx'].ravel()[1])
					cv2.drawContours(img, [dot['approx']], 0, color, 1)
					cv2.putText(img, "{}".format(dot['no']), org, font, 0.4, color)

		### QDの周辺部
		color = (255, 0, 0)
		for _, dot in enumerate(self.dots, 1):
			xmin, ymin = dot['approx'].max(axis=1).min(axis=0)
			xmax, ymax = dot['approx'].max(axis=1).max(axis=0)
			rect = np.array([[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]])
			dot['rect'] = rect
			if self.states['rect']:
				if dot['marker'] == '1':
					org = (dot['approx'].ravel()[0], dot['approx'].ravel()[1])
					cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 1)
					cv2.putText(img, "{}".format(dot['no']), org, font, 0.4, color)

		color = (0, 0, 255)
		if self.states['marker']:
			if self.dots[self.row]['marker'] == '1':
				org = (self.dots[self.row]['approx'].ravel()[0], self.dots[self.row]['approx'].ravel()[1])
				cv2.drawContours(img, [self.dots[self.row]['approx']], 0, color, 1)
				cv2.putText(img, "{}".format(self.dots[self.row]['no']), org, font, 0.4, color)

		self.show_image(img[0:512, 0:512], self.m_panel3)
		self.img = img

	def counting(self):
		"""Count QDs"""
		# 平滑化
		base_img = cv2.medianBlur(self.base_img, self.params['blur'])

		# 二値化
		_, binary = cv2.threshold(base_img, self.params['threshold'], 255, cv2.THRESH_BINARY)
		binary = cv2.medianBlur(binary, self.params['medianBlur'])
		#binary = cv2.dilate(binary, np.ones((3, 3), np.uint8), iterations=1)

		# エッジ検出
		edges = cv2.Canny(base_img, threshold1=self.params['threshold1'], threshold2=self.params['threshold2'])
		edges = cv2.dilate(edges, np.ones((self.params['dilate'], self.params['dilate']), np.uint8), iterations=1)

		# 画像合成
		comp = cv2.bitwise_or(binary, edges)
		comp = cv2.Canny(comp, threshold1=50, threshold2=100)
		#comp = cv2.dilate(comp, np.ones((2, 2), np.uint8), iterations=1)
		self.show_image(comp, self.m_panel2)

		# 輪郭を抽出
		contours, hierarchy = cv2.findContours(comp, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

		# 背景画像(カラー)
		source = self.m_textCtrl1.GetValue()
		img = cv2.imread(source)

		# ピクセル取得用画像
		gray = cv2.imread(source, 0)
		croped = gray.copy()

		# QDのカウント
		self.dots = []
		color = (0, 255, 0)
		font = cv2.FONT_HERSHEY_DUPLEX
		for _, (cnt, hrc) in enumerate(zip(contours, hierarchy[0])):
			if hrc[3] >= 0:
				approx = cv2.approxPolyDP(cnt, 0.0000001*cv2.arcLength(cnt, True), True)
				if len(approx) > 6:
					area = 4 * cv2.contourArea(cnt)
					if area > self.params['area']:
						# 図形を数える
						org = (approx.ravel()[0], approx.ravel()[1])
						self.dots.append({'no': len(self.dots)+1, 'cnt': cnt, 'area': area, 'diameter': 2*np.sqrt(area/np.pi), 'approx': approx, 'marker': '1', 'created': False})
						cv2.drawContours(img, [approx], 0, color, 1)
						cv2.putText(img, "{}".format(len(self.dots)), org, font, 0.4, color)

		### QDの周辺部
		color = (255, 0, 0)
		for index, dot in enumerate(self.dots, 1):
			xmin, ymin = dot['approx'].max(axis=1).min(axis=0)
			xmax, ymax = dot['approx'].max(axis=1).max(axis=0)
			rect = np.array([[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]])
			dot['rect'] = rect
			if self.states['rect']:
				org = (dot['approx'].ravel()[0], dot['approx'].ravel()[1])
				cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 1)
				cv2.putText(img, "{}".format(dot['no']), org, font, 0.4, color)
		self.show_image(img[0:512, 0:512], self.m_panel3)
		self.img = img

		### QDのパラメーター抽出
		for index, dot in enumerate(self.dots, 1):
			#底面の高さ
			mask1 = np.zeros(croped.shape[:2], np.uint8)
			cv2.drawContours(mask1, [dot['rect']], -1, (255, 255, 255), -1, cv2.LINE_AA)
			background = np.ones_like(croped, np.uint8)*255
			cv2.bitwise_not(background, background, mask=mask1)
			dst1 = background + cv2.bitwise_and(croped, croped, mask=mask1)

			mask2 = 255*np.ones(croped.shape[:2], np.uint8)
			cv2.drawContours(mask2, [dot['approx']], -1, (0, 0, 0), -1, cv2.LINE_AA)
			background = np.ones_like(croped, np.uint8)*255
			cv2.bitwise_not(background, background, mask=mask2)
			dst2 = background + cv2.bitwise_and(dst1, dst1, mask=mask2)

			bottom = np.average(dst2[dst2 < 255])

			#最大の高さ
			cv2.drawContours(mask1, [dot['approx']], -1, (255, 255, 255), -1, cv2.LINE_AA)
			dst3 = cv2.bitwise_and(croped, croped, mask=mask1)
			top = dst3.max()

			#QD高さ
			dot['height'] = (top - bottom)/255 * self.params['height']

		### QDの数の結果
		#print('Number of circle = ', len(self.dots))
		self.m_grid1.DeleteRows(pos=0, numRows=self.m_grid1.GetNumberRows())
		self.m_grid1.AppendRows(len(self.dots))
		for index, dot in enumerate(self.dots):
			self.m_grid1.SetCellValue(index, 0, '{}'.format(int(dot['area'])))
			self.m_grid1.SetCellValue(index, 1, '{:.2}'.format(dot['height']))
			self.m_grid1.SetCellRenderer(index, 2, wx.grid.GridCellBoolRenderer())
			self.m_grid1.SetCellEditor(index, 2, wx.grid.GridCellBoolEditor())
			self.m_grid1.SetCellValue(index, 2, dot['marker'])

		self.m_grid2.DeleteRows(pos=0, numRows=self.m_grid2.GetNumberRows())
		self.m_grid2.AppendRows(len(self.params))
		for index, (key, value) in enumerate(self.params.items()):
			self.m_grid2.SetCellValue(index, 0, '{}'.format(key))
			self.m_grid2.SetCellValue(index, 1, '{}'.format(value))

		self.row = -1

	# Handlers for MyFrame1 events.
	def m_button1OnButtonClick(self, event):
		dialog = wx.FileDialog(None, u'Select Image', style=wx.FD_OPEN)
		dialog.ShowModal()
		self.path = dialog.GetPath()
		self.cmap = self.path.rsplit(os.sep, 1)[0]+os.sep + 'cmap'+os.sep+self.path.rsplit(os.sep, 1)[1]
		self.output_tif = self.path.rsplit(os.sep, 1)[0]+os.sep + 'output'+os.sep+self.path.rsplit(os.sep, 1)[1]
		self.output_csv = self.output_tif.rsplit(".")[0]+'.csv'
		self.output_json = self.output_tif.rsplit(".")[0]+'.json'
		self.dots_json = self.output_tif.rsplit(".")[0]+'_dots.json'
		self.output_dir, _ = (self.output_tif).rsplit(os.sep, 1)
		self.m_textCtrl1.SetValue(self.path)
		self.m_textCtrl2.SetValue(self.cmap)
		source_img = cv2.imread(self.m_textCtrl1.GetValue())

		# color map画像読み込み
		self.org_img = cv2.imread(self.cmap, 0)
		self.base_img = self.org_img[0:512, 0:512]
		self.show_image(source_img[570:590, 480:520], self.m_panel4, 1)
		self.counting()

	def m_slider2OnScroll(self, event):
		self.params['blur'] = 2*self.m_slider2.GetValue()-1
		self.counting()

	def m_spinCtrl5OnTextEnter(self, event):
		self.params['threshold'] = self.m_spinCtrl5.GetValue()
		self.counting()

	def m_slider4OnScroll(self, event):
		self.params['medianBlur'] = 2*self.m_slider4.GetValue()-1
		self.counting()

	def m_spinCtrl1OnTextEnter(self, event):
		self.params['threshold1'] = self.m_spinCtrl1.GetValue()
		self.counting()

	def m_spinCtrl2OnTextEnter(self, event):
		self.params['threshold2'] = self.m_spinCtrl2.GetValue()
		self.counting()

	def m_slider5OnScroll(self, event):
		self.params['dilate'] = 2*self.m_slider5.GetValue()-1
		self.counting()

	def m_spinCtrl3OnTextEnter(self, event):
		self.params['area'] = self.m_spinCtrl3.GetValue()
		self.counting()

	def m_spinCtrlDouble1OnSpinCtrlText(self, event):
		self.params['height'] = self.m_spinCtrlDouble1.GetValue()
		dots_disp = []
		for dot in self.dots:
			dots_disp.append(dot['marker'])
		self.counting()
		for index, flag in enumerate(dots_disp):
			self.dots[index]['marker'] = flag
			self.m_grid1.SetCellValue(index, 2, flag)
		self.rendering()

	def m_checkBox1OnCheckBox(self, event):
		self.states['marker'] = self.m_checkBox1.GetValue()
		self.rendering()

	def m_checkBox2OnCheckBox(self, event):
		self.states['rect'] = self.m_checkBox2.GetValue()
		self.rendering()

	def m_button2OnButtonClick(self, event):
		if not os.path.exists(self.output_dir):
			os.mkdir(self.output_dir)

		dots_disp = []
		output_dots = [["No", "area [nm2]", "height [nm]", "diameter [nm]"]]
		for dot in self.dots:
			dots_disp.append(dot['marker'])
			if dot['marker'] == '1':
				output_dots.append([dot['no'], dot['area'], dot['height'], dot['diameter']])
		with open(self.output_csv, 'w', newline='') as book:
			csv.writer(book).writerows(output_dots)
		with open(self.output_json, 'w') as paramsfile:
			json.dump({'params': self.params, 'dots': dots_disp}, paramsfile)
		# 結果の画像作成
		cv2.imwrite(self.output_tif, self.img)

	def m_button3OnButtonClick(self, event):
		with open(self.output_json, "r") as json_file:
			json_obj = json.load(json_file)
			self.params = json_obj['params']
			self.m_slider2.SetValue(int((self.params['blur']+1)/2))
			self.m_spinCtrl5.SetValue(self.params['threshold'])
			self.m_slider4.SetValue(int((self.params['medianBlur']+1)/2))
			self.m_spinCtrl1.SetValue(self.params['threshold1'])
			self.m_spinCtrl2.SetValue(self.params['threshold2'])
			self.m_slider5.SetValue(int((self.params['dilate']+1)/2))
			self.m_spinCtrl3.SetValue(self.params['area'])
			self.m_spinCtrlDouble1.SetValue(self.params['height'])
			self.counting()

			dots_disp = json_obj['dots']
			for index, flag in enumerate(dots_disp):
				self.dots[index]['marker'] = flag
				self.m_grid1.SetCellValue(index, 2, flag)
			self.rendering()

	def m_grid1OnGridSelectCell(self, event):
		if self.row == event.Row:
			if self.dots[self.row]['created']:
				self.dots[self.row]['marker'] = '0' if self.m_grid1.GetCellValue(self.row, 2) == '1' else '1'
			else:
				self.dots[self.row]['marker'] = '1' if self.dots[self.row]['marker'] == '1' else '0'
		else:
			self.row = event.Row
		self.rendering()

	def m_grid1OnGridEditorCreated(self, event):
		if event.Col == 2:
			event.Control.Bind(wx.EVT_CHECKBOX, self.onCheckBox)
			self.dots[self.row]['created'] = True
			self.dots[self.row]['marker'] = '1' if self.dots[self.row]['marker'] != '1' else '0'
			self.rendering()

	def onCheckBox(self, evt):
		"""Checkbox event in grid"""
		row = self.m_grid1.GridCursorRow
		self.dots[row]['marker'] = '1' if evt.IsChecked() else '0'
		self.rendering()

	def m_spinCtrl4OnSpinCtrlText(self, event):
		self.row = self.m_spinCtrl4.GetValue()-1
		self.rendering()

	def m_spinCtrl4OnTextEnter(self, event):
		self.row = self.m_spinCtrl4.GetValue()-1
		self.dots[self.row]['marker'] = '1' if self.dots[self.row]['marker'] != '1' else '0'
		self.m_grid1.SetCellValue(self.row, 2, self.dots[self.row]['marker'])
		self.rendering()
