---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.41
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.29
    win_rate: 0.42
    alternates:
    - name: Ancient Signet
      pick_rate: 0.13
      win_rate: 0.63
    - name: Runeforged Hammer
      pick_rate: 0.09
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.38
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.22
      win_rate: 0.53
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.46
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.34
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.56
  - name: Obsidian Shard
    pick_rate: 0.1
    win_rate: 0.48
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.62
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.29
  - name: Dwarven Plate
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.36
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.5
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.03
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.31
    win_rate: 0.37
  - name: Bluestone Brooch
    pick_rate: 0.29
    win_rate: 0.59
  - name: Sands Of Time
    pick_rate: 0.13
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-19'
  god_win_rate: 0.48881789137380194
  god_matches_won: 153
  god_matches_played: 313
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Kinetic Cuirass, The Crusher,
    Amanita Charm, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge, Golden Blade,
    Nimble Ring, Eye of the Storm, Oni Hunter''s Garb, Pharaoh''s Curse, Hydra''s
    Lament, Shield Splitter, Shield of the Phoenix, Avenging Blade, Spectral Armor,
    Lernaean Bow, Erosion, Eye of Providence, Death Metal, Shogun''s Ofuda, Draconic
    Scale, Damaru, Leviathan''s Hide, Soul Gem, Midgardian Mail, Breastplate of Valor,
    Tyrfing, Triton''s Conch, The Reaper, Rod of Asclepius, Hide of the Nemean Lion,
    Yogi''s Necklace, Wyrmskin Hide, Bragi''s Harp, Ancile, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.09
      fit: 0.56
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.56
      pick: 0.2
      fit: 0.29
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Kinetic Cuirass,
    Berserker''s Shield, Rod of Tahuti, Gluttonous Grimoire, The Crusher, Soul Gem,
    Rod of Asclepius, Oni Hunter''s Garb, Jotunn''s Revenge, The Reaper, Chandra''s
    Grace, Eye of the Storm, Golden Blade, Pharaoh''s Curse, Erosion, Nimble Ring,
    Shield Splitter, Phoenix Feather, Eye of Providence, Spectral Armor, Draconic
    Scale, Riptalon, Hydra''s Lament, Shogun''s Ofuda, Avenging Blade, Leviathan''s
    Hide, Midgardian Mail, Blood-Bound Book, Lifebinder, Breastplate of Valor, Lernaean
    Bow, Bancroft''s Talon, Death Metal, Ancile, Damaru, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.71
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.59
      pick: 0.09
      fit: 0.53
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.56
      pick: 0.2
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Jotunn''s Revenge,
    Runeforged Hammer, Soul Gem, Berserker''s Shield, Avenging Blade, Kinetic Cuirass,
    Amanita Charm, The Reaper, The Cosmic Horror, Nimble Ring, Spear of the Magus,
    Void Shield, Riptalon, Stone of Binding, Screeching Gargoyle, Oni Hunter''s Garb,
    Tekko-Kagi, Silverbranch Bow, Golden Blade, Void Stone, Spear of Desolation, Hydra''s
    Lament, Heartseeker, Pharaoh''s Curse, Eye of the Storm, Toxic Blade, Spectral
    Armor, Shield of the Phoenix, Titan''s Bane, Shield Splitter, Lernaean Bow, Death
    Metal, Breastplate of Valor, Erosion, Pendulum Blade, Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.72
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.59
      pick: 0.09
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Runeforged Hammer
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Gluttonous Grimoire
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Nimble Ring, Runeforged Hammer, Golden Blade, Rod
    of Tahuti, Gluttonous Grimoire, Kinetic Cuirass, Riptalon, The Crusher, Amanita
    Charm, Pharaoh''s Curse, Tyrfing, Jotunn''s Revenge, Silverbranch Bow, Lernaean
    Bow, Oni Hunter''s Garb, Shogun''s Ofuda, Soul Gem, Toxic Blade, Spectral Armor,
    Hydra''s Lament, Shield of the Phoenix, Breastplate of Valor, Eye of the Storm,
    Erosion, Eros'' Bow, Shield Splitter, Bragi''s Harp, Leviathan''s Hide, Eye of
    Providence, Death Metal, Avenging Blade, Bracer of The Abyss, Dominance, Midgardian
    Mail, The Reaper, Yogi''s Necklace, Damaru, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.36
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.55
      win: 0.59
      pick: 0.09
      fit: 0.36
    Freya's Tears:
      total: 0.5
      efficiency: 0.59
      win: 0.56
      pick: 0.2
      fit: 0.19
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Runeforged Hammer, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire, Hydra''s
    Lament, Berserker''s Shield, Breastplate of Valor, Kinetic Cuirass, Nimble Ring,
    Amanita Charm, The Crusher, Genji''s Guard, Chronos'' Pendant, Chandra''s Grace,
    Spear of Desolation, Screeching Gargoyle, Oni Hunter''s Garb, Gladiator''s Shield,
    Pharaoh''s Curse, Gem of Focus, Spectral Armor, Golden Blade, Totem of Death,
    Arondight, Erosion, Rod of Asclepius, Death Metal, Prophetic Cloak, Eye of the
    Storm, The Cosmic Horror, Eye of Providence, Leviathan''s Hide, Shogun''s Ofuda,
    Helm of Radiance, Midgardian Mail, Spear of the Magus, Jade Scepter.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.55
      win: 0.59
      pick: 0.09
      fit: 0.34
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.2
      fit: 0.52
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, The Crusher, Amanita
    Charm, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge, Runeforged Hammer,
    Golden Blade, Genji''s Guard, Nimble Ring, Eye of the Storm, Oni Hunter''s Garb,
    Pharaoh''s Curse, Hydra''s Lament, Shield Splitter, Shield of the Phoenix, Avenging
    Blade, Spectral Armor, Lernaean Bow, Erosion, Breastplate of Valor, Eye of Providence,
    Death Metal, Shogun''s Ofuda, Draconic Scale, Damaru, Leviathan''s Hide, Soul
    Gem, Midgardian Mail, Tyrfing, Triton''s Conch, The Reaper, Rod of Asclepius,
    Yogi''s Necklace, Wyrmskin Hide, Bragi''s Harp, Ancile, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.09
      fit: 0.56
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
---
