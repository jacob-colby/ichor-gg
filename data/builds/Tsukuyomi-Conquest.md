---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.5
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.37
    win_rate: 0.37
    alternates:
    - name: Transcendence
      pick_rate: 0.35
      win_rate: 0.5
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.5
  - name: Transcendence
    pick_rate: 0.27
    win_rate: 0.35
    alternates:
    - name: Book of Thoth
      pick_rate: 0.19
      win_rate: 0.57
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.44
  - name: Hydra's Lament
    pick_rate: 0.24
    win_rate: 0.52
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.21
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.54
  - name: Heartseeker
    pick_rate: 0.28
    win_rate: 0.45
    alternates:
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.58
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.55
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.41
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.44
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.43
  - name: Lucerne Hammer
    pick_rate: 0.17
    win_rate: 0.42
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.1
      win_rate: 0.43
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.2
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.43
    win_rate: 0.55
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.26
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-08-27'
  god_win_rate: 0.4435483870967742
  god_matches_won: 55
  god_matches_played: 124
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch Bow, Lernaean
    Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus, Spear of Desolation,
    Riptalon, Obsidian Shard, Dominance, Deathbringer, Soul Gem, The Reaper, Toxic
    Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss, Musashi''s Dual
    Swords, Doom Orb, Avatar''s Parashu, The World Stone, Pendulum Blade, Arondight,
    Runeforged Hammer, Qin''s Blade, Dreamer''s Idol, Damaru, Rage, Ancient Signet,
    Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.07
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.49
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.35
      pick: 0.37
      fit: 0.24
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.39
    The Crusher:
      total: 0.5
      efficiency: 0.47
      win: 0.55
      pick: 0.15
      fit: 0.54
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.45
      pick: 0.47
      fit: 0.64
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the
    Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow, Doom Orb, Tekko-Kagi,
    Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant, Silverbranch
    Bow, Dominance, Bracer of The Abyss, Golden Blade, Dreamer''s Idol, Deathbringer,
    The Reaper, Arondight, Gem of Focus, Polynomicon, Pendulum Blade, Riptalon, Runeforged
    Hammer, Musashi''s Dual Swords, Soul Reaver, Avatar''s Parashu, Rod of Asclepius,
    The Cosmic Horror, Toxic Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.28
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.52
    Transcendence:
      total: 0.4
      efficiency: 0.53
      win: 0.35
      pick: 0.37
      fit: 0.28
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.49
    Death Metal:
      total: 0.49
      efficiency: 0.61
      win: 0.42
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.42
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Spear of Desolation, Death Metal, Soul Gem, Spear of the Magus,
    Obsidian Shard, Nimble Ring, Silverbranch Bow, Tekko-Kagi, Gluttonous Grimoire,
    Doom Orb, Tyrfing, Lernaean Bow, Bragi''s Harp, The World Stone, Chronos'' Pendant,
    Dreamer''s Idol, The Reaper, Riptalon, Pendulum Blade, Bracer of The Abyss, Ancient
    Signet, Toxic Blade, Golden Blade, Arondight, Gem of Focus, Deathbringer, Dominance,
    Avatar''s Parashu, The Cosmic Horror, Musashi''s Dual Swords, Runeforged Hammer,
    Rod of Asclepius, Totem of Death, Demon Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.16
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.56
    Transcendence:
      total: 0.38
      efficiency: 0.53
      win: 0.35
      pick: 0.37
      fit: 0.16
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.42
    The Crusher:
      total: 0.49
      efficiency: 0.47
      win: 0.55
      pick: 0.15
      fit: 0.5
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.42
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Soul Gem, Golden Blade, Death Metal, The Reaper,
    Riptalon, Runeforged Hammer, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard,
    Shifter''s Shield, Breastplate of Valor, Shield Splitter, Ethereal Staff, Yogi''s
    Necklace, Eye of the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix Feather,
    Erosion, Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow, Eye of Providence,
    Spear of the Magus, Lifebinder, Draconic Scale, Tekko-Kagi, Avenging Blade, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.04
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.42
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.3
    Transcendence:
      total: 0.38
      efficiency: 0.53
      win: 0.35
      pick: 0.37
      fit: 0.15
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.27
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Tekko-Kagi, Silverbranch Bow, Spear of the Magus,
    Death Metal, Spear of Desolation, Obsidian Shard, Soul Gem, Riptalon, The Reaper,
    Gluttonous Grimoire, Tyrfing, Toxic Blade, Lernaean Bow, Doom Orb, The World Stone,
    Nimble Ring, Avatar''s Parashu, Avenging Blade, Dreamer''s Idol, Pendulum Blade,
    Golden Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic Horror, Bracer
    of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, The Executioner,
    Runeforged Hammer, Arondight, Ancient Signet, Chronos'' Pendant, Qin''s Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.05
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.6
    Transcendence:
      total: 0.39
      efficiency: 0.53
      win: 0.35
      pick: 0.37
      fit: 0.19
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.32
    The Crusher:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.15
      fit: 0.67
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.45
      pick: 0.47
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Nimble Ring
  - Riptalon
  flex_slots:
  - Tyrfing
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade,
    The Reaper, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian Shard, Spear
    of Desolation, Dominance, Bracer of The Abyss, Qin''s Blade, Deathbringer, Demon
    Blade, Doom Orb, The World Stone, Ancient Signet, Blood-Bound Book, Sun Beam Bow,
    Dreamer''s Idol, Chronos'' Pendant, Musashi''s Dual Swords, Runeforged Hammer,
    Arondight, Berserker''s Shield, Avatar''s Parashu, Bancroft''s Talon, Pendulum
    Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.05
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.3
    Tyrfing:
      total: 0.46
      efficiency: 0.48
      win: 0.42
      pick: 0.0
      fit: 0.66
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.27
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.42
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.47
      efficiency: 0.51
      win: 0.42
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Silverbranch
    Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean Bow, Pendulum
    Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss, Totem
    of Death, Doom Orb, Riptalon, Golden Blade, The World Stone, Ancient Signet, Breastplate
    of Valor, Dreamer''s Idol, Deathbringer, Dominance, Toxic Blade, Genji''s Guard,
    The Reaper, Qin''s Blade, Musashi''s Dual Swords, Runeforged Hammer, Demon Blade,
    Avatar''s Parashu.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.1
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.59
    Transcendence:
      total: 0.38
      efficiency: 0.53
      win: 0.35
      pick: 0.37
      fit: 0.1
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.55
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.42
      pick: 0.0
      fit: 0.24
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Spear of Desolation,
    Soul Gem, Spear of the Magus, Nimble Ring, Obsidian Shard, Bragi''s Harp, Gluttonous
    Grimoire, Chronos'' Pendant, Doom Orb, Silverbranch Bow, Tyrfing, Lernaean Bow,
    Tekko-Kagi, Bracer of The Abyss, The World Stone, Dreamer''s Idol, Ancient Signet,
    Gem of Focus, Golden Blade, The Reaper, Riptalon, Deathbringer, Dominance, Arondight,
    The Cosmic Horror, Pendulum Blade, Rod of Asclepius, Toxic Blade, Polynomicon,
    Totem of Death, Avatar''s Parashu, Blood-Bound Book, Musashi''s Dual Swords.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.25
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.46
    Transcendence:
      total: 0.38
      efficiency: 0.53
      win: 0.35
      pick: 0.37
      fit: 0.16
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.39
    Death Metal:
      total: 0.49
      efficiency: 0.61
      win: 0.42
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.42
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Death Metal
  - The Crusher
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Spear
    of the Magus, Nimble Ring, Spear of Desolation, Obsidian Shard, Bragi''s Harp,
    Soul Gem, Tekko-Kagi, Tyrfing, Lernaean Bow, Gluttonous Grimoire, Silverbranch
    Bow, Doom Orb, Bracer of The Abyss, The World Stone, Golden Blade, Dreamer''s
    Idol, The Reaper, Ancient Signet, Dominance, Deathbringer, Chronos'' Pendant,
    Riptalon, Toxic Blade, Avatar''s Parashu, Musashi''s Dual Swords, Demon Blade,
    The Cosmic Horror, Runeforged Hammer, Arondight, Pendulum Blade, Gem of Focus,
    Rod of Asclepius, Polynomicon.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.57
      pick: 0.26
      fit: 0.22
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.44
    Transcendence:
      total: 0.39
      efficiency: 0.53
      win: 0.35
      pick: 0.37
      fit: 0.22
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.52
      pick: 0.37
      fit: 0.36
    Death Metal:
      total: 0.49
      efficiency: 0.61
      win: 0.42
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.5
      efficiency: 0.47
      win: 0.55
      pick: 0.15
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch
    Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Spear of Desolation, Riptalon, Obsidian Shard, Dominance, Deathbringer, Soul Gem,
    The Reaper, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Doom Orb, Avatar''s Parashu, The World Stone, Pendulum
    Blade, Arondight, Runeforged Hammer, Qin''s Blade, Dreamer''s Idol, Damaru, Rage,
    Ancient Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.37
      pick: 0.37
      fit: 0.49
    Tyrfing:
      total: 0.47
      efficiency: 0.48
      win: 0.42
      pick: 0.0
      fit: 0.72
    Death Metal:
      total: 0.48
      efficiency: 0.61
      win: 0.42
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.46
      efficiency: 0.53
      win: 0.42
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.47
      efficiency: 0.49
      win: 0.42
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.42
      pick: 0.0
      fit: 0.27
  starter: *id001
---
