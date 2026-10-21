---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.69
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.33
    win_rate: 0.68
    alternates:
    - name: Stampede
      pick_rate: 0.21
      win_rate: 0.58
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.8
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.63
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.75
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.16
    win_rate: 0.44
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.67
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.25
  - name: Genji's Guard
    pick_rate: 0.09
    win_rate: 0.8
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.83
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.8
  - name: Rod of Tahuti
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.33
  - name: Captain's Ring
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Veve Charm
      pick_rate: 0.09
      win_rate: 0.67
    - name: Brawler’s Beat Stick
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.93
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.38
  - name: Heroism
    pick_rate: 0.19
    win_rate: 0.73
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-10-21'
  god_win_rate: 0.6206896551724138
  god_matches_won: 36
  god_matches_played: 58
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Hydra''s Lament, Shifter''s Shield,
    Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Hide of the
    Nemean Lion, Prophetic Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Spear of Desolation, Spectral
    Armor, Hussar''s Wings, Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel,
    Soul Gem, Doublet of Binding, Rod of Tahuti.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.68
      efficiency: 0.42
      win: 1.0
      pick: 0.18
      fit: 0.49
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.15
      fit: 0.37
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.78
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.8
      pick: 0.09
      fit: 0.29
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.19
      fit: 0.62
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Hydra's Lament
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Shifter''s Shield, Jotunn''s Revenge, Soul Gem, Breastplate of Valor, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather,
    Gluttonous Grimoire, Yogi''s Necklace, Shield Splitter, Chandra''s Grace, Runeforged
    Hammer, Glorious Pridwen, Eye of the Storm, Lifebinder, Midgardian Mail, Stone
    of Binding, Hide of the Nemean Lion, Helm of Radiance, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Sphere of Negation,
    Screeching Gargoyle, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s
    Shield, Rod of Tahuti.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.67
      efficiency: 0.42
      win: 1.0
      pick: 0.18
      fit: 0.41
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.15
      fit: 0.34
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.9
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.8
      pick: 0.09
      fit: 0.3
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Hydra''s Lament,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Void Shield, Spear of the Magus, Soul Gem, Breastplate of Valor, Void Stone, Shifter''s
    Shield, Obsidian Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion,
    Shield Splitter, Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom
    Orb, Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s Bane, Magi''s
    Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, Midgardian
    Mail, The Reaper, Daybreak Gavel, Hide of the Nemean Lion, Rod of Asclepius, Leviathan''s
    Hide, Rod of Tahuti.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.18
      fit: 0.34
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.15
      fit: 0.26
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.47
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.8
      pick: 0.09
      fit: 0.23
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
  - Hydra's Lament
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Hydra''s Lament, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Breastplate of
    Valor, Tyrfing, Shifter''s Shield, Shield Splitter, Soul Gem, Runeforged Hammer,
    Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion,
    Helm of Radiance, Eye of Providence, Stone of Binding, Eye of the Storm, Shield
    of the Phoenix, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s
    Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging
    Blade, Rod of Tahuti.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.54
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.18
      fit: 0.26
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.15
      fit: 0.2
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.8
      pick: 0.09
      fit: 0.27
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hydra's Lament
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear
    of Desolation, Screeching Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant,
    Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Helm of Radiance,
    Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of Focus, Magi''s
    Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Obsidian
    Shard, Hide of the Nemean Lion, Leviathan''s Hide, Jade Scepter, Void Shield,
    Rod of Tahuti.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.18
      fit: 0.32
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.8
      pick: 0.15
      fit: 0.48
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.19
      fit: 0.64
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.8
      pick: 0.09
      fit: 0.52
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Freya's Tears
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Brawler’s Beat Stick
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Breastplate
    of Valor, Golden Blade, Shifter''s Shield, Eye of the Storm, Gluttonous Grimoire,
    Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Spear of the Magus, Eye of Providence, Avenging Blade, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Helm of Radiance, Soul Gem, Titan''s Bane, Silverbranch
    Bow, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s Cloak, Toxic Blade,
    The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord,
    Midgardian Mail, Rod of Tahuti.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.18
      fit: 0.3
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.67
      pick: 0.14
      fit: 0.04
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.15
      fit: 0.23
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.45
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.62
      efficiency: 0.54
      win: 0.8
      pick: 0.09
      fit: 0.4
  community_ordered:
  - Brawler’s Beat Stick
  - Book of Thoth
  - Genji's Guard
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Brawler’s Beat Stick
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Breastplate
    of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Soul Gem, Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye
    of the Storm, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield
    of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail, Rod
    of Tahuti.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.18
      fit: 0.3
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.67
      pick: 0.14
      fit: 0.18
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.15
      fit: 0.23
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.18
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.8
      pick: 0.09
      fit: 0.36
  community_ordered:
  - Brawler’s Beat Stick
  - Book of Thoth
  - Genji's Guard
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Hide of the
    Nemean Lion, Prophetic Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Spear of Desolation, Spectral
    Armor, Hussar''s Wings, Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel,
    Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.15
      fit: 0.37
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.19
      fit: 0.62
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
