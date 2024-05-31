document.addEventListener('DOMContentLoaded', function() {
    fetch('./menu.json')
.then(response => response.json())
.then(data => {
            const currentMonth = new Date().getMonth();
            const testMode = true; // Set to false once testing is done
            let targetMonth = currentMonth + 1; 
            if (testMode) {
              targetMonth = 6; // Setting to 6 for June (since May is treated as June for testing)
            }

            const parentContainer = document.querySelector('.daily-menu-parent-container');
            const menuSubtitle = document.querySelector('.menu-subtitle');
            const months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'};
            menuSubtitle.textContent = months[targetMonth] + "'s Menu";

            if (data[targetMonth]) { 
                data[targetMonth].forEach(dayData => {
                    const dayContainer = document.createElement('div');
                    dayContainer.classList.add('menu-day-container');
                    const dateTitle = document.createElement('h3');
                    dateTitle.classList.add('date-title');
                    dateTitle.textContent = dayData.dayName;

                    const dayNumber = document.createElement('p');
                    dayNumber.textContent = dayData.day.toString().padStart(2, '0'); 
                    const dateBar = document.createElement('div');
                    dateBar.classList.add('date-bar');
                    dateBar.appendChild(dateTitle);
                    dateBar.appendChild(dayNumber);
                    dayContainer.appendChild(dateBar);

                    const dailyMenu = document.createElement('div');
                    dailyMenu.classList.add('daily-menu');
                    ['morning', 'afternoon', 'snacks'].forEach(mealType => {
                        const mealLabel = document.createElement('h3');
                        if (mealType === 'snacks') {
                            mealLabel.textContent = "Snack:"; 
                        } else {
                            mealLabel.textContent = `${mealType} Meal:`; 
                        }
                        const mealList = document.createElement('ul');
                        if (dayData.hasOwnProperty(mealType.toLowerCase())) {
                            dayData[mealType.toLowerCase()].forEach(item => {
                                const listItem = document.createElement('li');
                                listItem.textContent = item;
                                mealList.appendChild(listItem);
                            });
                        } else {
                            console.warn(`Key "${mealType}" not found in dayData`);
                        }
                        dailyMenu.appendChild(mealLabel);
                        dailyMenu.appendChild(mealList);
                    });

                    dayContainer.appendChild(dailyMenu);
                    parentContainer.appendChild(dayContainer);
                });
            } else {
                console.log(`No data found for ${targetMonth}`);
            }
        })
.catch(error => console.error('Error fetching JSON:', error));
});
