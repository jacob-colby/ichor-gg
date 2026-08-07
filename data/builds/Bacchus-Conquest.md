---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.36
    win_rate: 0.47
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.48
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.51
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.7
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.7
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.6
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.48
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.65
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.85
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.65
    alternates:
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.47
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.21
    win_rate: 0.54
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.4
  - name: Sundering Axe
    pick_rate: 0.15
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-08-07'
  god_win_rate: 0.5267034990791897
  god_matches_won: 286
  god_matches_played: 543
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-07'
  god_matches_analyzed: 13100
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Berserker's Shield
  - Kinetic Cuirass
  - Prophetic Cloak
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Freya''s Tears, Oni Hunter''s Garb, Gluttonous Grimoire, Stampede, Shield
    of the Phoenix, Erosion, Breastplate of Valor, Spectral Armor, Shield Splitter,
    Pharaoh''s Curse, Jotunn''s Revenge, Runeforged Hammer, The Crusher, Leviathan''s
    Hide, Soul Gem, Eye of the Storm, Hydra''s Lament, Mantle Of Discord, Hide of
    the Nemean Lion, Stone of Binding, Midgardian Mail, Yogi''s Necklace, Shogun''s
    Ofuda, Helm of Radiance, Magi''s Cloak, Ancile, Rod of Asclepius, Gladiator''s
    Shield, Doublet of Binding, Xibalban Effigy, Void Shield, Hussar''s Wings, Screeching
    Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.48
      pick: 0.06
      fit: 0.78
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.43
      win: 0.7
      pick: 0.08
      fit: 0.62
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.63
      pick: 0.06
      fit: 0.68
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Shield of the Phoenix, Kinetic Cuirass,
    Eye of Providence, Berserker''s Shield, Soul Gem, Gluttonous Grimoire, Rod of
    Asclepius, Oni Hunter''s Garb, Stampede, Chandra''s Grace, Freya''s Tears, Erosion,
    Breastplate of Valor, Phoenix Feather, Spectral Armor, Runeforged Hammer, Pharaoh''s
    Curse, Jotunn''s Revenge, Lifebinder, Yogi''s Necklace, Leviathan''s Hide, Eye
    of the Storm, The Crusher, Blood-Bound Book, Hide of the Nemean Lion, Midgardian
    Mail, Shield Splitter, Bancroft''s Talon, Hydra''s Lament, Glorious Pridwen, Shogun''s
    Ofuda, The Reaper, Ancile, Gladiator''s Shield, Riptalon, Jade Scepter.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.66
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.48
      pick: 0.06
      fit: 0.76
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.43
      win: 0.7
      pick: 0.08
      fit: 0.54
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.9
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.63
      pick: 0.06
      fit: 0.66
    Amanita Charm:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Draconic Scale, Amanita Charm, Jotunn''s Revenge,
    The Crusher, Berserker''s Shield, Soul Gem, Kinetic Cuirass, Eye of Providence,
    Stone of Binding, Oni Hunter''s Garb, Screeching Gargoyle, Freya''s Tears, Spear
    of the Magus, Void Shield, Avenging Blade, Breastplate of Valor, The Cosmic Horror,
    Void Stone, Shield of the Phoenix, Spear of Desolation, Erosion, Spectral Armor,
    Runeforged Hammer, Pharaoh''s Curse, Hydra''s Lament, Yogi''s Necklace, Obsidian
    Shard, Riptalon, Shield Splitter, The Reaper, Silverbranch Bow, Leviathan''s Hide,
    Helm of Radiance, Midgardian Mail, Eye of the Storm, Rod of Asclepius, Mantle
    Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Prophetic Cloak:
      total: 0.53
      efficiency: 0.43
      win: 0.7
      pick: 0.08
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.06
      fit: 0.48
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Prophetic Cloak
  - Draconic Scale
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Draconic Scale, Amanita Charm, Gluttonous Grimoire,
    Kinetic Cuirass, Golden Blade, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s
    Garb, The Crusher, Jotunn''s Revenge, Riptalon, Runeforged Hammer, Breastplate
    of Valor, Freya''s Tears, Lernaean Bow, Hydra''s Lament, Soul Gem, Shogun''s Ofuda,
    Shield of the Phoenix, Tyrfing, Spectral Armor, Silverbranch Bow, Yogi''s Necklace,
    Shield Splitter, Erosion, Eye of the Storm, Bracer of The Abyss, Dominance, Death
    Metal, Leviathan''s Hide, Rod of Asclepius, Helm of Radiance, Avenging Blade,
    Bragi''s Harp, Midgardian Mail, Damaru, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Prophetic Cloak:
      total: 0.52
      efficiency: 0.43
      win: 0.7
      pick: 0.08
      fit: 0.33
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.63
      pick: 0.06
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Prophetic Cloak, Draconic Scale, Freya''s
    Tears, Amanita Charm, Breastplate of Valor, Jotunn''s Revenge, Shield of the Phoenix,
    Berserker''s Shield, Hydra''s Lament, Soul Gem, Kinetic Cuirass, Gluttonous Grimoire,
    Eye of Providence, Oni Hunter''s Garb, The Crusher, Chronos'' Pendant, Runeforged
    Hammer, Screeching Gargoyle, Chandra''s Grace, Spear of Desolation, Gladiator''s
    Shield, Spectral Armor, Erosion, Shield Splitter, Yogi''s Necklace, Pharaoh''s
    Curse, Helm of Radiance, Rod of Asclepius, Gem of Focus, Eye of the Storm, Arondight,
    Death Metal, Leviathan''s Hide, Hide of the Nemean Lion, Jade Scepter, Midgardian
    Mail, Spear of the Magus, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.18
      fit: 0.48
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.11
      fit: 0.48
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.43
      win: 0.7
      pick: 0.08
      fit: 0.64
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.06
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Draconic Scale
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, Draconic Scale, The Crusher,
    Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Eye of
    Providence, Runeforged Hammer, Hydra''s Lament, Oni Hunter''s Garb, Shield Splitter,
    Freya''s Tears, Soul Gem, Breastplate of Valor, Golden Blade, Lernaean Bow, Eye
    of the Storm, Pharaoh''s Curse, Shield of the Phoenix, Death Metal, Spectral Armor,
    Avenging Blade, Erosion, Yogi''s Necklace, The Reaper, Damaru, Spear of the Magus,
    Shogun''s Ofuda, Leviathan''s Hide, Dominance, The Cosmic Horror, Helm of Radiance,
    Heartseeker, Rod of Asclepius, Riptalon, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Prophetic Cloak:
      total: 0.52
      efficiency: 0.43
      win: 0.7
      pick: 0.08
      fit: 0.38
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.06
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Draconic Scale,
    Amanita Charm, The Crusher, Jotunn''s Revenge, Berserker''s Shield, Soul Gem,
    Kinetic Cuirass, Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s
    Lament, Death Metal, Freya''s Tears, Spear of the Magus, Breastplate of Valor,
    Shield Splitter, The Cosmic Horror, Helm of Radiance, Shield of the Phoenix, Rod
    of Asclepius, Eye of the Storm, Spectral Armor, Erosion, Spear of Desolation,
    Jade Scepter, Yogi''s Necklace, Pharaoh''s Curse, Avenging Blade, Golden Blade,
    Obsidian Shard, Lernaean Bow, The Reaper, Triton''s Conch, Chronos'' Pendant,
    Damaru, Leviathan''s Hide, Wish-Granting Pearl.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Prophetic Cloak:
      total: 0.52
      efficiency: 0.43
      win: 0.7
      pick: 0.08
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.06
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Freya''s Tears, Oni Hunter''s Garb, Gluttonous Grimoire, Shield of the
    Phoenix, Erosion, Breastplate of Valor, Draconic Scale, Spectral Armor, Shield
    Splitter, Pharaoh''s Curse, Jotunn''s Revenge, Runeforged Hammer, The Crusher,
    Leviathan''s Hide, Soul Gem, Eye of the Storm, Hydra''s Lament, Mantle Of Discord,
    Stone of Binding, Midgardian Mail, Yogi''s Necklace, Hide of the Nemean Lion,
    Shogun''s Ofuda, Helm of Radiance, Magi''s Cloak, Stampede, Ancile, Rod of Asclepius,
    Gladiator''s Shield, Doublet of Binding, Xibalban Effigy, Void Shield, Hussar''s
    Wings, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.18
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.48
      pick: 0.06
      fit: 0.78
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
---
