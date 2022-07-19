function week_translator(input, seg)
   if (input == "yweek" || input == "zweek") then
      if (os.date("%w") == "0") then
         weekstr = "日"
         week_de = "Sonntag"
      end
      if (os.date("%w") == "1") then
         weekstr = "一"
         week_de = "Montag"
      end
      if (os.date("%w") == "2") then
         weekstr = "二"
         week_de = "Dienstag"
      end
      if (os.date("%w") == "3") then
         weekstr = "三"
         week_de = "Mittwoch"
      end
      if (os.date("%w") == "4") then
         weekstr = "四"
         week_de = "Donnerstag"
      end
      if (os.date("%w") == "5") then
         weekstr = "五"
         week_de = "Freitag"
      end
      if (os.date("%w") == "6") then
         weekstr = "六"
         week_de = "Samstag"
      end
      yield(Candidate("qsj", seg.start, seg._end, "星期"..weekstr, "[星期]"))
      yield(Candidate("qsj", seg.start, seg._end, "禮拜"..weekstr, "[星期]"))
      yield(Candidate("qsj", seg.start, seg._end, week_de, "[星期]"))
      yield(Candidate("date", seg.start, seg._end, os.date("%A"), "[星期]"))
   end
end
return week_translator
